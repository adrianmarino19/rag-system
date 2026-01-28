#!/usr/bin/env python3

import argparse
import json

# Save all movies in a dictionary
with open("data/movies.json", "r") as file:
    movies_dic = json.load(file)

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}")

            # Inneficient for loop to check every single title. 
            for movie in movies_dic['movies']:
                for word in movie['title'].split(' '):
                    if word == str(args.query):
                        print(movie['title'])
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()

# it works but without caps lock!