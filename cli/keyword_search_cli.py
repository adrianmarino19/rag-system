import argparse
import json
import sys
from pathlib import Path

from lib.keyword_search import (
    InvertedSearch,
    build_command,
    search_command,
    tf_command,
    idf_command,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    build_parser = subparsers.add_parser("build", help="Build inverted index")

    tf_parser = subparsers.add_parser("tf", help="Build inverted index")
    tf_parser.add_argument("doc_id", type=int, help="Movie ID")
    tf_parser.add_argument("term", type=str, help="Term to look for in Movie ID")

    idf_parser = subparsers.add_parser("idf", help="Build inverted index")
    idf_parser.add_argument("term", type=str, help="Term to used for calculation")

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

        case "tf":
            results = tf_command(args.doc_id, args.term)
            if results:
                print(f"Your term appears {results} time(s) in ID {args.doc_id}")

        case "idf":
            result = idf_command(args.term)
            print(f"Inverse document frequency of '{args.term}': {result:.2f}")

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
