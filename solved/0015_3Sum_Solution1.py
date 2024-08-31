# region Quest
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
#Notice that the solution set must not contain duplicate triplets.
#
# 
#
#Example 1:
#
#Input: nums = [-1,0,1,2,-1,-4]
#Output: [[-1,-1,2],[-1,0,1]]
#Explanation: 
#nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#The distinct triplets are [-1,0,1] and [-1,-1,2].
#Notice that the order of the output and the order of the triplets does not matter.
#Example 2:
#
#Input: nums = [0,1,1]
#Output: []
#Explanation: The only possible triplet does not sum up to 0.
#Example 3:
#
#Input: nums = [0,0,0]
#Output: [[0,0,0]]
#Explanation: The only possible triplet sums up to 0.
# endregion


from typing import List

# Solution to slow. Time Limit Exceeded

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        List = []
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    stack = [nums[i], nums[j], nums[k]]
                    stack = sorted(stack)
                    if nums[i] + nums[j] + nums[k] == 0 and stack not in List:
                        List.append(stack)
        return List

solution = Solution()

nums = [9,-9,4,12,12,0,-14,-7,10,-1,11,-10,-3,2,-9,0,8,-9,-5,-1,10,5,13,-5,-9,-12,9,-3,10,10,-10,4,8,1,-7,-2,-14,-6,6,11,8,-6,9,13,11,7,-10,-4,14,0,3,1,-10,-7,3,-12,-3,-11,0,-8,-15,5,3,8,13,11,13,-15,-9,4,3,6,5,-11,-4,-6,4,1,5,-5,-13,-7,11,-8,2,-1,-12,14,3,3,13,-5,-14,-7,11,14,-11,9,6,-13,-9,-13,1,11,-9,12,-10,2,-1,3,12,-7,3,0,0,12,6,3,3,-13,14,1,-3]
print(solution.threeSum(nums))  #Output:
nums = [-1,0,1,2,-1,-4]
print(solution.threeSum(nums))  #Output: [[-1,-1,2],[-1,0,1]]
nums = [0,1,1]
print(solution.threeSum(nums))  #Output: []
nums = [0,0,0]
print(solution.threeSum(nums))  #Output: [[0,0,0]]