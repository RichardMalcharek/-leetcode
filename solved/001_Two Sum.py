# region Quest
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# You can return the answer in any order.
# 
# Example 1:
# 
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# 
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# 
# Input: nums = [3,3], target = 6
# Output: [0,1]
#  
# 
# Constraints:
# 
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
# endregion

nums = [3,3]
target = 6

for x in nums:
    I1 = nums.index(x)
    try:
        I2 = nums[I1+1:].index(target-x)+I1+1                
        if I1 != I2 and x + nums[I2] == target: 
            print(I1, I2) 
            #return [I1, I2]  
        continue
    except:
        continue

