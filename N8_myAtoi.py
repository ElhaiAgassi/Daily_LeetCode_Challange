#Runtime: 33 ms, faster than 93.96% of Python3 online submissions for String to Integer (atoi).
#Memory Usage: 13.9 MB, less than 78.55% of Python3 online submissions for String to Integer (atoi).

import math

class Sol:
    def in_rng(self, num: int, pos) -> int:
        maxint: int = int(math.pow(2, 31))-1
        minint: int = -1 - maxint
        num = int(num)*pos
        if num < minint:
            return minint
        elif num > maxint:
            return maxint
        else:
            return num

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s or len(s) < 2 and not s[0].isnumeric():
            return 0
        ans, pos, = "", 1

        pos = -1 if s[0] == '-' else 1
        if (s[0] in ['-','+']):
            s = s[1:]
        if not s[0].isnumeric():
            return 0
        found = False
        for c in range(0, len(s), +1):
            if found and not s[c].isnumeric():
                return self.in_rng(int(ans),pos)
            if s[c].isnumeric():
                found = True
                ans += s[c]

        return self.in_rng(int(ans),pos)




this = Sol()
print(Sol.myAtoi(this, "-91283472332"))
