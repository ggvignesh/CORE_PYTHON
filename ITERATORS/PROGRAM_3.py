class EvenNumbers:
    def __init__(self, n):
        self.count = 0
        self.n = n
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.count < self.n:
            self.num += 2
            self.count += 1
            return self.num
        raise StopIteration

n = int(input())
obj1 = EvenNumbers(n)
k = iter(obj1)
for i in k:
    print(i)