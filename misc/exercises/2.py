exercise_2 = """
Goal

Feel why grouping data and functions matters.

Task

Create a class called Notebook.

Rules:
It stores a list of notes (strings)
It has:
add_note(text)
all_notes() → returns the list
count() → number of notes

Then:
Create one notebook
Add 3 notes
Print the count
Print the notes
Constraint (important)

You are not allowed to store the notes outside the class.
"""


class Notebook:
    def __init__(self):
        self.all_notes = []

    def add_note(self, text):
        self.all_notes.append(text)

    def count(self):
        return len(self.all_notes)


notebook_1 = Notebook()

notebook_1.add_note("hello")
notebook_1.add_note("I am")
notebook_1.add_note("the best")

if __name__ == "__main__":
    print(notebook_1.count())
    for note in notebook_1.all_notes:
        print(note)
