# region Quest
#Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.
#Since the result may be very large, so you need to return a string instead of an integer.
#
#Example 1:
#
#Input: nums = [10,2]
#Output: "210"
#
#Example 2:
#
#Input: nums = [3,30,34,5,9]
#Output: "9534330"
# 
#
#Constraints:
#
#1 <= nums.length <= 100
#0 <= nums[i] <= 109
# endregion


import time
from typing import Optional, List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(str, nums))

        nums.sort(key=lambda x: x*10, reverse=True)


        return str(int(''.join(map(str, nums))))
    

solution = Solution()

nums = [3,30,34,5,9]
Output = "9534330"  
result = solution.largestNumber(nums)
print(f'{result==Output} : {result}')

nums = [10,2,9,39,17]
Output = "93921710"
result = solution.largestNumber(nums)
print(f'{result==Output} : {result}')

nums = [0,0]
Output = "0"
result = solution.largestNumber(nums)
print(f'{result==Output} : {result}')

nums = [10,2]
Output = "210"
result = solution.largestNumber(nums)
print(f'{result==Output} : {result}')

nums = [432,43243]
Output = "43243432"
result = solution.largestNumber(nums)
print(f'{result==Output} : {result}')