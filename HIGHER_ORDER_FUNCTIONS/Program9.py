#9. What happens if the lambda passed to reduce() accepts only one parameter or three parameters? Explain the output or error.
#One Parameter
from functools import reduce
nums = [1,2,3]
reduce(lambda x: x, nums)

#Three Parameters
from functools import reduce
nums = [1,2,3]
reduce(lambda x, y, z: x+y+z, nums)