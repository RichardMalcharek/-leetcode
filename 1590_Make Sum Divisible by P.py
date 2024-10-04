
from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rest = sum(nums)%p
        if rest == 0:
            return 0
        result = float('inf')

        for i in range(0,len(nums)):
            if result == 1:
                break
            for j in range(i+1, len(nums)+1):
                if j-i > result:
                    break
                if sum(nums[i:j])%p == rest:
                    result = min(result, j-i)
        if result == float('inf') or result == len(nums):
            return -1
        else:
            return result

solution = Solution()

nums = [1,2,3]
p = 7
Output = -1
result = solution.minSubarray(nums, p)
print(f'{result==Output} : {result}')

nums = [3,1,4,2]
p = 6
Output = 1
result = solution.minSubarray(nums, p)
print(f'{result==Output} : {result}')

nums = [6,3,5,2]
p = 9
Output = 2
result = solution.minSubarray(nums, p)
print(f'{result==Output} : {result}')

nums = [1,2,3]
p = 3
Output = 0
result = solution.minSubarray(nums, p)
print(f'{result==Output} : {result}')