def lengthOfLongestSubstring(s: str) -> int:
    # sub = ''
    # maximum = 0
    # for i in s:
    #     if (i in sub):
    #         sub = sub[sub.index(i)+1:]+i
    #     else:
    #         sub = sub+i
    #   maximum = max(maximum,len(sub))
    # return maximum

    map = {}
    left = max_length = 0
    for right, c in enumerate(s):
        if (c in map):
            left = max(left, map[c]+1)
        max_length = max(max_length, right - left +1)
        map[c] = right
    return max_length


st = "tmmzuxt"
print(lengthOfLongestSubstring(st))
