import math
from typing import List
import numpy


# Solutin 1/3  Two pointers and map
def maximumUniqueSubarray(nums: List[int]) -> int:

    max_sub, curr_sum ,start, end = 0, 0 , 0, 0
    curr_list = {}

    while start <= end and end < len(nums):
        if nums[end] not in curr_list:
            curr_list[nums[end]] = end
            curr_sum += nums[end]
            end += 1
        else:
            while nums[end] in curr_list:
                curr_sum -= nums[start]
                del curr_list[nums[start]]
                start += 1
        max_sub = max(max_sub, curr_sum)
    return max_sub


# Solutin 2/3 Two pointers and boolean array

# def maximumUniqueSubarray(nums: List[int]) -> int:
# max_sub = 0
# curr_list = numpy.full(int(math.pow(10, 5)), False, dtype=bool)
# curr_sum, start, end = 0, 0, 0
# while start <= end and end < len(nums):
#     if curr_list[nums[end]]:
#         while curr_list[nums[end]]:
#             curr_sum -= nums[start]
#             curr_list[nums[start]] = False
#             start += 1
#     else:
#         curr_list[nums[end]] = True
#         curr_sum += nums[end]
#         end += 1
#     max_sub = max(max_sub, curr_sum)


# Solution 3/3 Two pointers map and prefix sum array

# def maximumUniqueSubarray(nums: List[int]) -> int:
#     map_list, prefix_list = {}, [0] * (len(nums) + 1)
#     max_sub, start, end = 0, 0, 0
#     while start <= end < len(nums):
#         current_number = nums[end]
#         prefix_list[end + 1] = prefix_list[end] + current_number
#
#         if current_number in map_list:
#             start = max(start, map_list[current_number] + 1)
#
#         max_sub = max(max_sub, prefix_list[end + 1] - prefix_list[start])
#         map_list[current_number] = end
#         end += 1
#     return max_sub

# print(maximumUniqueSubarray(#[4, 2, 4, 4, 5]))
# [187, 470, 25, 436, 538, 809, 441, 167, 477, 110, 275, 133, 666, 345, 411, 459, 490, 266, 987, 965, 429, 166, 809,
#  340, 467, 318, 125, 165, 809, 610, 31, 585, 970, 306, 42, 189, 169, 743, 78, 810, 70, 382, 367, 490, 787, 670, 476,
#  278, 775, 673, 299, 19, 893, 817, 971, 458, 409, 886, 434]))
