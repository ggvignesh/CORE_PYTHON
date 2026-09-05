class OddNumbers:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.lst):
            n = self.lst[self.index]
            self.index += 1
            if n % 2 != 0:
                return n
        raise StopIteration

lst = list(map(int, input().split()))
obj1 = OddNumbers(lst)
k = iter(obj1)
for i in k:
    print(i)