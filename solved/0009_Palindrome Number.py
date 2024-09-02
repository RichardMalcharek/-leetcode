# region Quest
#Given an integer x, return true if x is a 
#palindrome
#, and false otherwise.
#
# 
#
#Example 1:
#
#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
#Example 2:
#
#Input: x = -121
#Output: false
#Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#Example 3:
#
#Input: x = 10
#Output: false
#Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
#
#Constraints:
#
#-231 <= x <= 231 - 1
# endregion


import time
from typing import Optional, List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
    

solution = Solution()

x = 121
print(solution.isPalindrome(x))     # Output: true
x = -121
print(solution.isPalindrome(x))     # Output: false
x = 10
print(solution.isPalindrome(x))     # Output: false
