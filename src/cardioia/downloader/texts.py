"""
Text downloader and normalizer.

This module:
- downloads text sources from configured URLs
- extracts readable text from HTML
- extracts text from PDF
- stores normalized .txt files
- tracks already downloaded content in SQLite
"""

from __future__ import annotations

from io import BytesIO
from pathlib import Path
from typing import Any

import requests
import trafilatura
from pypdf import PdfReader

from cardioia.state import ManifestDB
from cardioia.utils import ensure_dir, sanitize_filename


def _extract_text_from_pdf(content: bytes) -> str:
    """
    Extract text from a PDF byte stream.
    """
    reader = PdfReader(BytesIO(content))
    parts: list[str] = []
    for page in reader.pages:
        extracted = page.extract_text() or ""
        if extracted.strip():
            parts.append(extracted)
    return "\n".join(parts).strip()


def _extract_text_from_html(content: str) -> str:
    """
    Extract readable text from HTML using trafilatura.
    """
    extracted = trafilatura.extract(content, include_comments=False, include_tables=True)
    return (extracted or "").strip()


def _download_text_content(url: str) -> tuple[bytes, str]:
    """
    Download raw content and return bytes + content-type.
    """
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    return response.content, response.headers.get("Content-Type", "")


def run_texts(config: dict[str, Any], count: int) -> None:
    """
    Execute text download pipeline.

    Parameters
    ----------
    config : dict[str, Any]
        Loaded YAML configuration.
    count : int
        Number of text files to download/process.
    """
    paths = config["paths"]
    text_cfg = config["texts"]

    output_dir = ensure_dir(paths["text_dir"])
    manifest = ManifestDB(paths["state_db"])

    processed = 0
    for item in text_cfg["sources"]:
        if processed >= count:
            break

        name = item["name"]
        url = item["url"]
        resource_id = sanitize_filename(name)

        if manifest.exists("text", resource_id):
            print(f"[SKIP] Already downloaded: {resource_id}")
            continue

        try:
            raw_content, content_type = _download_text_content(url)

            text = ""
            if "pdf" in content_type.lower() or url.lower().endswith(".pdf"):
                text = _extract_text_from_pdf(raw_content)
            else:
                text = _extract_text_from_html(raw_content.decode("utf-8", errors="ignore"))

            if not text.strip():
                raise ValueError("No textual content could be extracted.")

            target_path = output_dir / f"{resource_id}.txt"
            target_path.write_text(text, encoding="utf-8")

            manifest.add("text", resource_id, url, str(target_path))
            processed += 1
            print(f"[OK] Text downloaded: {resource_id}")

        except Exception as exc:
            print(f"[WARN] Failed to process text source '{name}': {exc}")

    manifest.close()
    print(f"[DONE] Text pipeline finished. Files generated: {processed}")
