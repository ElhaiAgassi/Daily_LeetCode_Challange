from typing import List


class Solution:
    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        for i in range(n+m-1,-1,-1):
            if n-1 < 0: break
            if m>0 and nums1[m-1] >= nums2[n-1]:
                nums1[i] = nums1[m-1]
                m-=1
            else:
                nums1[i] = nums2[n-1]
                n-=1


    # merge([1,2,3,0,0,0],3,[2,5,6], 3)
#Runtime: 55 ms, faster than 41.99% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.8 MB, less than 85.45% of Python3 online submissions for Merge Sorted Array.
