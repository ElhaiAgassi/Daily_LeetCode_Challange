# Runtime: 170 ms, faster than 20.42% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.2 MB, less than 67.40% of Python3 online submissions for Median of Two Sorted Arrays.

from typing import List


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        find_kth = staticmethod(Solution.find_kth)
        total = len(nums1) + len(nums2)
        print(total)
        if total % 2 == 1:  # if odd we have one median
            return find_kth(nums1, nums2, total // 2)
        else:  # if even we have two median
            return (find_kth(nums1, nums2, total // 2 - 1) + find_kth(nums1, nums2, total // 2)) / 2

    @staticmethod
    def find_kth(ls1: List[int], ls2: List[int], k: int) -> float:
        find_kth = staticmethod(Solution.find_kth)
        if not ls1:
            return ls2[k]
        if not ls2:
            return ls1[k]
        idxl1, idxl2 = len(ls1) // 2, len(ls2) // 2
        medl1, medl2 = ls1[idxl1], ls2[idxl2]

        if idxl1 + idxl2 < k:
            if medl1 > medl2:
                return find_kth(ls1, ls2[idxl2 + 1:], k - idxl2 - 1)
            else:
                return find_kth(ls1[idxl1 + 1:], ls2, k - idxl1 - 1)
        else:  # if k is smaller than the middles together
            if medl1 > medl2:
                return find_kth(ls1[:idxl1], ls2, k)
            else:
                return find_kth(ls1, ls2[:idxl2], k)
