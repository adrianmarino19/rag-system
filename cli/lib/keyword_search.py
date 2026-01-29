from .search_utils import DEFAULT_SEARCH_LIMIT,  load_movies


def search_command(query: str, limit: int = DEFAULT_SEARCH_LIMIT) -> list[dict]:
    movies = load_movies()
    results = []
    preproc_query = preprocessing(query)

    for movie in movies:
        preproc_title = preprocessing(movie['title'])
        if preproc_query in preproc_title:
            results.append(movie)
            if len(results) >= limit:
                break
    return results


def preprocessing(text: str) -> str:
    text = text.lower()
    return text



# Remember to use 'in' in Python. Much faster!