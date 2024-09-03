# region Quest
#Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
#0 <= a, b, c, d < n
#a, b, c, and d are distinct.
#nums[a] + nums[b] + nums[c] + nums[d] == target
#You may return the answer in any order.
#
# 
#
#Example 1:
#
#Input: nums = [1,0,-1,0,-2,2], target = 0
#Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#Example 2:
#
#Input: nums = [2,2,2,2,2], target = 8
#Output: [[2,2,2,2]]
# 
#
#Constraints:
#
#1 <= nums.length <= 200
#-109 <= nums[i] <= 109
#-109 <= target <= 109
# endregion


#Constraints:
#
#1 <= nums.length <= 200
#-109 <= nums[i] <= 109
#-109 <= target <= 109

import time
from typing import Optional, List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        List = []

        for i in range(0,len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(len(nums)-1,i+2, -1):
                if j < len(nums)-1 and nums[j] == nums[j+1]:
                    continue
                left, right = i+1, j-1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        List.append([nums[i],nums[left],nums[right], nums[j]])

                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -=1

                        left += 1
                        right -= 1
                    
        return List
    

solution = Solution()

nums = [1,0,-1,0,-2,2]
target = 0
print(solution.fourSum(nums, target))   #   Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

nums = [2,2,2,2,2]
target = 8
print(solution.fourSum(nums, target))   # Output: [[2,2,2,2]]
