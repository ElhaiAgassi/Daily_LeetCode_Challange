#Runtime: 33 ms, faster than 89.75% of Python3 online submissions for Reverse Integer.
#Memory Usage: 13.8 MB, less than 96.96% of Python3 online submissions for Reverse Integer.

import math


def reverse(x: int) -> int:
    x = int(str(x)[::-1]) if x >= 0 else -int((str(x)[1:])[::-1])
    if x <= (math.pow(2, 31)) and x >= (0-math.pow(2, 31)):
        return x
    return 0


print(reverse(1534236469))
