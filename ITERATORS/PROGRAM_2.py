class ReverseNumbers:
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= 1:
            n = self.start
            self.start -= 1
            return n
        raise StopIteration

n = int(input())
obj1 = ReverseNumbers(n)
k = iter(obj1)
for i in k:
    print(i,end=" ")