class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence[::-1]
        self.number = number
        self.counter = len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration

        if self.counter > 0:
            self.counter -= 1
        else:
            self.counter = len(self.sequence) - 1
        self.number -= 1
        return self.sequence[self.counter]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')