from typing import List

# Runtime: 66 ms, faster than 86.13% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 14.42% of Python3 online submissions for Two Sum.

class N1_two_sum:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range(len(nums)):
            remaining = target - nums[i]

            if remaining in my_map:
                return [my_map[remaining], i]
            else:
                my_map[nums[i]] = i

    print(twoSum([1, 2, 3], int(4)))
