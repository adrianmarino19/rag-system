import os
import pickle
from collections import defaultdict
from pathlib import Path

import nltk
import spacy
from spacy.tokens import Token

from .search_utils import (
    CACHE_DIR,
    DEFAULT_SEARCH_LIMIT,
    PROJECT_ROOT,
    STOPWORDS,
    load_movies,
    nlp,
)

nlp = spacy.load("en_core_web_sm")


class InvertedSearch:
    """
    An inverted index for fast document retrieval based on keywords.

    The index maps lemmatized terms to lists of document IDs containing those terms.
    """

    def __init__(self):
        """Initialize an empty inverted index and document map."""
        self.index: dict[str, list[int]] = defaultdict(list)
        self.docmap: dict[int, dict] = {}
        self.index_path = os.path.join(CACHE_DIR, "index.pkl")
        self.docmap_path = os.path.join(CACHE_DIR, "docmap.pkl")

    def build(self) -> None:
        """
        Build the inverted index from all movies in the dataset.

        Loads all movies and indexes their titles and descriptions.
        """
        movies = load_movies()

        for movie in movies:
            doc_id = movie["id"]
            text = f"{movie['title']} {movie['description']}"
            self.__add_documents(doc_id, text, movie)

    def __add_documents(self, doc_id: int, text: str, movie: dict) -> None:
        """
        Add a document to the inverted index (private method).

        Args:
            doc_id: Unique identifier for the document
            text: The text content to index
        """
        self.docmap[doc_id] = movie

        doc = nlp(text)
        for token in doc:
            lemma = token.lemma_.lower()
            if (
                not token.is_punct
                and token.text.lower() not in STOPWORDS
                and doc_id not in self.index[lemma]
            ):
                self.index[lemma].append(doc_id)

    def get_documents(self, term: str) -> list[int] | None:
        """
        Retrieve document IDs containing the given term.

        Args:
            term: The search term to look up

        Returns:
            List of document IDs, or None if term not found
        """
        preproc_term = "".join(preprocessing(term))
        if preproc_term in self.index:
            return self.index[preproc_term]
        else:
            return None

    def save(self) -> None:
        """Save the inverted index and dictionary to disk."""
        CACHE_DIR.mkdir(exist_ok=True)

        with open(self.index_path, "wb") as f:
            pickle.dump(self.index, f)

        with open(self.docmap_path, "wb") as f:
            pickle.dump(self.docmap, f)

    def load(self) -> None:
        """Load the inverted index and document map from disk."""
        with open(self.index_path, "rb") as f:
            self.index = pickle.load(f)

        with open(self.docmap_path, "rb") as f:
            self.docmap = pickle.load(f)


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    """
    Search for movies matching the query.

    Args:
        query: Search query string
        limit: Maximum number of results to return (default: DEFAULT_SEARCH_LIMIT)

    Returns:
        List of movie dictionaries matching the query
    """
    preproc_query = preprocessing(query)

    idx = InvertedSearch()
    idx.load()

    results = []
    for word in preproc_query:
        all_doc_ids = idx.get_documents(word)
        if not all_doc_ids:
            continue
        for doc_id in all_doc_ids:
            if doc_id not in results:
                results.append(idx.docmap[doc_id])
                if len(results) >= limit:
                    return results

    return results


def build_command():
    print("Building inverted index...")
    idx = InvertedSearch()
    idx.build()
    print("Saving index...")
    idx.save()
    return idx


def matching_token(query_tokens: str, title_tokens: str) -> bool:
    """
    Check if any query token matches any title token (substring match).

    Args:
        query_tokens: List of preprocessed tokens from the query
        title_tokens: List of preprocessed tokens from the title

    Returns:
        True if any query token is found as a substring in any title token, False otherwise
    """
    for query_token in query_tokens:
        for title_token in title_tokens:
            if query_token in title_token:
                return True
    return False


def preprocessing(text: str) -> list[str]:
    """
    Preprocess a document (more than one word). Return the stemmatized word as a string if it is not
    a stopword or punctuation, otherwise return None.
    """
    doc = nlp(text)

    tokens = []
    for token in doc:
        # Skip punctuation and stopwords
        if not token.is_punct and token.text.lower() not in STOPWORDS:
            tokens.append(token.lemma_.lower())  # Append stemmatized word.
    return tokens
