from .search_utils import DEFAULT_SEARCH_LIMIT, load_movies
from string import punctuation
import spacy


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    preproc_query = preprocessing(query)

    for movie in movies:
        preproc_title = preprocessing(movie["title"])
        if matching_token(preproc_query, preproc_title):
            results.append(movie)
            if len(results) >= limit:
                break
    return results


def matching_token(query_tokens: str, title_tokens: str) -> bool:
    for query_token in query_tokens:
        for title_token in title_tokens:
            if query_token in title_token:
                return True
    return False


def preprocessing(text: str) -> list[str]:
    text = text.lower().translate(str.maketrans("", "", punctuation))
    tokens = text.split()
    return tokens


# Remember to use 'in' in Python. Much faster!
## You must compare IN vs string directly to understand if it's substring.
