from typing import List


def findMedianSortedArrays( nums1: List[int], nums2: List[int]) -> float:
    ans : float = 0
    total = (len(nums1)+len(nums2))
    if not total%2: # if even 2 median
        print(total)
    nums3 = nums1
    print(nums3)

findMedianSortedArrays([1,2,3],[4,5,6])