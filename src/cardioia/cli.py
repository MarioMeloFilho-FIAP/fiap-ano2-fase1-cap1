"""
Author: OpenAI
Version: 1.0.0

CLI entrypoint for CardioIA Fase 1 project.
"""

from __future__ import annotations

import argparse

from cardioia.config import load_yaml_config
from cardioia.downloader.ptbxl import run_ptbxl
from cardioia.downloader.texts import run_texts


def build_parser() -> argparse.ArgumentParser:
    """
    Build CLI parser.
    """
    parser = argparse.ArgumentParser(
        prog="cardioia",
        description="CLI para coleta de dados do projeto CardioIA - Fase 1.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    ptbxl_parser = subparsers.add_parser(
        "ptbxl",
        help="Baixa metadados PTB-XL, gera dataset numérico e imagens de ECG.",
    )
    ptbxl_parser.add_argument(
        "--config",
        required=True,
        help="Caminho para o arquivo YAML de configuração do PTB-XL.",
    )
    ptbxl_parser.add_argument(
        "--count",
        type=int,
        default=100,
        help="Número de exames/imagens a processar.",
    )

    texts_parser = subparsers.add_parser(
        "texts",
        help="Baixa e converte fontes textuais para .txt.",
    )
    texts_parser.add_argument(
        "--config",
        required=True,
        help="Caminho para o arquivo YAML de configuração textual.",
    )
    texts_parser.add_argument(
        "--count",
        type=int,
        default=2,
        help="Número de textos a baixar/processar.",
    )

    return parser


def main() -> None:
    """
    Main CLI function.
    """
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "ptbxl":
        config = load_yaml_config(args.config)
        run_ptbxl(config=config, count=args.count)
    elif args.command == "texts":
        config = load_yaml_config(args.config)
        run_texts(config=config, count=args.count)


if __name__ == "__main__":
    main()
