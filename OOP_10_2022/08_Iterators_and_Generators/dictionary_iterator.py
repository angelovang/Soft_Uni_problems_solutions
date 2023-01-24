class dictionary_iter:

    def __init__(self, dict):
        self.my_dict = list(dict.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.my_dict)-1:
            raise StopIteration

        self.index += 1
        result = self.my_dict[self.index]
        return result


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
