class ReverseCharacters:
    def __init__(self, string):
        self.string = string
        self.index = len(string) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= 0:
            ch = self.string[self.index]
            self.index -= 1
            return ch
        raise StopIteration

string = input()
obj1 = ReverseCharacters(string)
k = iter(obj1)
for i in k:
    print(i)