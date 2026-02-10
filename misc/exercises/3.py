import spacy

nlp = spacy.load("en_core_web_sm")

STOPWORDS = nlp.Defaults.stop_words

exercise_3 = """
This one prepares you directly for your assignment, without solving it.

Goal

Understand public vs private responsibility inside a class.

Task
Create a class called TextStats.
Rules:

It has:
a dictionary mapping words → counts
It has a method add_text(text)
Internally, it must use a helper method to:
tokenize the text
update counts

Example behavior:
Add "hello world"
Add "hello again"
Ask for count of "hello" → returns 2
"""


class TextStats:
    def __init__(self):
        self.dictionary = {}

    def add_text(self, text):
        tokens = self._tokenize_text(text)

        for token in tokens:
            if token in self.dictionary.keys():
                self.dictionary[token] += 1
            else:
                self.dictionary[token] = 1

    def _tokenize_text(self, text):
        doc = nlp(text)

        tokens = []
        for token in doc:
            # Skip punctuation and stopwords
            if not token.is_punct:
                tokens.append(token.lemma_.lower())  # Append stemmatized word.
        return tokens


dictionary_1 = TextStats()

dictionary_1.add_text("hello there")
dictionary_1.add_text("hello again")


if __name__ == "__main__":
    print(dictionary_1.dictionary)
