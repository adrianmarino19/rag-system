import argparse
import json
import sys
from pathlib import Path

from lib.keyword_search import InvertedSearch, build_command, search_command


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    build_parser = subparsers.add_parser("build", help="Build inverted index")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")

            results = search_command(args.query)
            for i, movie in enumerate(results, 1):
                print(f"{i}. {movie['id']} {movie['title']}")

        case "build":
            idx = build_command()
            docs = idx.get_documents("merida")
            print(f"First document for token 'merida' = {docs[0]}")

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
