#3. MathOps — Static Method
class MathOps:
    @staticmethod
    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False

print(MathOps.is_even(20))
M1 = MathOps()
print(M1.is_even(15))