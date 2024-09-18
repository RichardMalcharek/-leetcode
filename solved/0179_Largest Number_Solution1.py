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
        result = [nums[0]]
        for i in range(1,len(nums)):

            case1 = [nums[i]] + result
            
            for j in range(1,len(result)+1):
                case2 = result[:j] + [nums[i]] + result[j:]
                if  int(''.join(map(str, case1))) < int(''.join(map(str, case2))):
                    case1 = case2
            result = case1

        return str(int(''.join(map(str, result))))
    

solution = Solution()

nums = [0,0]
Output = "0"
result = solution.largestNumber(nums)
print(f'{result==Output} : {result}')

nums = [10,2,9,39,17]
Output = "93921710"
result = solution.largestNumber(nums)
print(f'{result==Output} : {result}')

nums = [10,2]
Output = "210"
result = solution.largestNumber(nums)
print(f'{result==Output} : {result}')

nums = [3,30,34,5,9]
Output = "9534330"
result = solution.largestNumber(nums)
print(f'{result==Output} : {result}')

nums = [432,43243]
Output = "43243432"
result = solution.largestNumber(nums)
print(f'{result==Output} : {result}')