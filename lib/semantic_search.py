from sentence_transformers import SentenceTransformer


class SemanticSearch:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)


# Outside of the class definition, create a new function called verify_model that creates an instance of the SemanticSearch class and prints the model information:
# Model loaded: {MODEL}, where {MODEL} is the .model string representation.
# Max sequence length: {MAX_LENGTH}, where {MAX_LENGTH} is the .max_seq_length property of the model.


def verify_model():
    search_instance = SemanticSearch()
    print(f"Model loaded: {search_instance.model}")
    print(f"Max sequence length: {search_instance.model.max_seq_length}")


if __name__ == "__main__":
    verify_model()
