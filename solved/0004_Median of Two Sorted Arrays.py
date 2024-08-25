# region Quest
#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
#The overall run time complexity should be O(log (m+n)).
#
# 
#
#Example 1:#
#
#Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
#Explanation: merged array = [1,2,3] and median is 2.
#Example 2:
#
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# endregion


from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        merge.sort()
        l = len(merge)
        if l%2 == 0:
            return (merge[(l-1)//2] + merge[((l-1)//2)+1])/2
        else:
            return merge[l//2]

solution = Solution()

nums1 = [1,3]
nums2 = [2]
print(solution.findMedianSortedArrays(nums1, nums2))     #Output: 2.00000


nums1 = [1,2]
nums2 = [3,4]
print(solution.findMedianSortedArrays(nums1, nums2))     #Output: 2.50000

nums1 = []
nums2 = [1]
print(solution.findMedianSortedArrays(nums1, nums2))     #Output: 1.00000

nums1 = [2]
nums2 = []
print(solution.findMedianSortedArrays(nums1, nums2))     #Output: 2.00000