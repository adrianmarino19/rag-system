#!/usr/bin/env python3

import argparse
import json

from lib.keyword_search import InvertedSearch, search_command


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")

            results = search_command(args.query)
            for i, movie in enumerate(results, start=1):
                print(f"{i}. {movie['title']}")

        case "build":
            print("Building dictionary...")

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()


# it works but without caps lock!
# perhaps put everything in Classes eh!
# why did the guy separate his files like that, why I didn't.
# What is an util.

# Perhaps I should build a project with them to understand their organization...
# And finish git this weekend!


# Que aprendimos?
## Comienza a poner type hints en todas las functions.
## Separa variables. Imaginate que es una aplicacion.


# No entiendas:
## os.path -> mas practica.
