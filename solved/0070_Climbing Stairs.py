# region Quest
#You are climbing a staircase. It takes n steps to reach the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# 
#
#Example 1:
#
#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#Example 2:
#
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
# endregion


import time
from typing import Optional, List

stairDict = {
    0 : 1,
    1 : 1
}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n in stairDict.keys():
            return stairDict[n]
        else:
            stairDict[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
            return stairDict[n]

    

solution = Solution()

n = 2 # = 2
print(solution.climbStairs(n))

n = 3 # = 3
print(solution.climbStairs(n))

n = 5 # = 8
print(solution.climbStairs(n))

