# region Quest
#You are given a string s. You can convert s to a 
# palindrome
# by adding characters in front of it.
#
#Return the shortest palindrome you can find by performing this transformation.
#
#Example 1:
#
#Input: s = "aacecaaa"
#Output: "aaacecaaa"
#Example 2:
#
#Input: s = "abcd"
#Output: "dcbabcd"
# 
#
#Constraints:
#
#0 <= s.length <= 5 * 104
#s consists of lowercase English letters only.
# endregion


import time
from typing import Optional, List

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        pointer = 0
        for i in range(len(s),0,-1):
            if s[:i] == s[i-1::-1]:
                pointer = i
                break
        return s[:pointer-1:-1]+s

solution = Solution()


s = "aacecaaa"
Output= "aaacecaaa"
result = solution.shortestPalindrome(s)
print(f'{result==Output} : {result}')

s = "abcd"
Output= "dcbabcd"
result = solution.shortestPalindrome(s)
print(f'{result==Output} : {result}')