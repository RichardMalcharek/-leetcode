# region Quest
#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
#
#You must not use any built-in exponent function or operator.
#
#For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# 
#
#Example 1:
#
#Input: x = 4
#Output: 2
#Explanation: The square root of 4 is 2, so we return 2.
#Example 2:
#
#Input: x = 8
#Output: 2
#Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
#endregion


import time
from typing import Optional, List

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        yn = 1
        while True:
            yx = (yn + (x/yn))/2
            if yx == yn:
                return int(yx)
            yn = yx


    

solution = Solution()

num = 4
print(solution.mySqrt(num))

num = 8
print(solution.mySqrt(num))