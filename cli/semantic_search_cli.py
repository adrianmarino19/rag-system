
import argparse
import os
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from lib.semantic_search import verify_model

def main():
    parser = argparse.ArgumentParser(description="Semantic Search CLI")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    subparsers.add_parser("verify", help="Verify that the embedding model is loaded")

    args = parser.parse_args()
    
    match args.command:
        case "verify":
            print("Verifying...")
            verify_model()
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()