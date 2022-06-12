# Runtime: 1952 ms, faster than 25.36% of Python3 online submissions for Minimum Operations to Reduce X to Zero.
# Memory Usage: 28 MB, less than 82.16% of Python3 online submissions for Minimum Operations to Reduce X to Zero.


from typing import List

def minOperations(nums: List[int], x: int) -> int:
    total, length = sum(nums), len(nums)
    left, curr, temp_max, solution = 0, 0, -1, False

    for right in range(length):
        curr += nums[right]
        while curr > total - x and left <= right:
            curr -= nums[left]
            left += 1
        if curr == total - x:
            temp_max = max(temp_max, right - left + 1)
            solution = True
    return length - temp_max if solution else -1
