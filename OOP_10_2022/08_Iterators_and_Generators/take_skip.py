class take_skip():

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.result = -step

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            raise StopIteration

        self.count -= 1
        self.result += self.step
        return self.result


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
