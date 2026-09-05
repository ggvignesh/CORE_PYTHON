class Characters:
    def __init__(self, string):
        self.string = string
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.string):
            ch = self.string[self.index]
            self.index += 1
            return ch
        raise StopIteration

string = input()
obj1 = Characters(string)
k = iter(obj1)
for i in k:
    print(i)