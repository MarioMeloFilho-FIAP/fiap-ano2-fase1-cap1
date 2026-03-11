"""
SQLite state management for downloaded resources.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path


class ManifestDB:
    """
    SQLite-backed manifest to track downloaded and processed resources.
    """

    def __init__(self, db_path: str) -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self._create_tables()

    def _create_tables(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS downloads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                resource_id TEXT NOT NULL,
                source_url TEXT,
                local_path TEXT,
                status TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(category, resource_id)
            )
            """
        )
        self.conn.commit()

    def exists(self, category: str, resource_id: str) -> bool:
        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT 1
            FROM downloads
            WHERE category = ? AND resource_id = ?
            LIMIT 1
            """,
            (category, resource_id),
        )
        return cursor.fetchone() is not None

    def add(
        self,
        category: str,
        resource_id: str,
        source_url: str,
        local_path: str,
        status: str = "completed",
    ) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            """
            INSERT OR IGNORE INTO downloads (category, resource_id, source_url, local_path, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (category, resource_id, source_url, local_path, status),
        )
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()
