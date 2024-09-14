# region Quest
#You are given an integer array nums of size n.
#Consider a non-empty subarray from nums that has the maximum possible bitwise AND.
#In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
#Return the length of the longest such subarray.
#The bitwise AND of an array is the bitwise AND of all the numbers in it.
#A subarray is a contiguous sequence of elements within an array.
#
#Example 1:
#
#Input: nums = [1,2,3,3,2,2]
#Output: 2
#Explanation:
#The maximum possible bitwise AND of a subarray is 3.
#The longest subarray with that value is [3,3], so we return 2.
#
#Example 2:
#
#Input: nums = [1,2,3,4]
#Output: 1
#Explanation:
#The maximum possible bitwise AND of a subarray is 4.
#The longest subarray with that value is [4], so we return 1.
# 
#
#Constraints:
#
#1 <= nums.length <= 105
#1 <= nums[i] <= 106
# endregion


from typing import  List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        amount = nums.count(target)
        if amount == 1:
            return 1
        
        count = 0
        result = 0
        for i in range(0,len(nums)):
            if nums[i] == target:
                count += 1
                result = max(result, count)
            else:
                count = 0
                if result >= amount/2:
                    break
        return result

    

solution = Solution()

nums = [1,2,3,3,2,2]
print(solution.longestSubarray(nums))   # Output: 2

nums = [1,2,3,4]
print(solution.longestSubarray(nums))   # Output: 1