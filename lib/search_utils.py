import json
import os
from pathlib import Path
from string import punctuation

import spacy

nlp = spacy.load("en_core_web_sm")

DEFAULT_SEARCH_LIMIT = 5
STOPWORDS = nlp.Defaults.stop_words

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "movies.json"
CACHE_DIR = PROJECT_ROOT / "cache"


# Save all movies in a dictionary
def load_movies() -> list[dict]:
    with DATA_PATH.open("r") as file:
        data = json.load(file)
    return data["movies"]
