exercise_1 = """
Task

Create a class called Counter.

Rules:
It starts at 0
It has a method increment() that adds 1
It has a method value() that returns the current number

Then:

Create two counters
Increment one twice
Increment the other once
Print both values
"""


class Counter:
    def __init__(self, balance):
        self.balance = balance

    def increment(self, value):
        self.balance += value


adrian = Counter(100)

seb = Counter(10)


if __name__ == "__main__":
    adrian.increment(100)
    adrian.increment(200)
    seb.increment(10)
    print(adrian.balance)
    print(seb.balance)
