class Numbers:
    def __init__(self, end):
        self.start = 0
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start < self.end:
            self.start += 1
            return self.start
        raise StopIteration

n = int(input())
obj1 = Numbers(n)
k = iter(obj1)
for i in k:
    print(i,end=" ")