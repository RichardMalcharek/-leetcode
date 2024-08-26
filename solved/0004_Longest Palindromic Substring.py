# region Quest
#Given a string s, return the longest 
#palindromic
# 
#substring
# in s.
#
# 
#
#Example 1:
#
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.
#Example 2:
#
#Input: s = "cbbd"
#Output: "bb"
# endregion


import time
from typing import Optional, List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        i = 0
        j = 0

        while i+len(result) < len(s):
            if s[i:j+1] == s[i:j+1][::-1]:
                if len(s[i:j+1]) > len(result):
                    result = s[i:j+1]
            j += 1
            if j >= len(s):
                i += 1
                j = i
        return result

solution = Solution()

s = "babad"
print(solution.longestPalindrome(s))    # Output: "bab"

s = "cbbd"
print(solution.longestPalindrome(s))    # Output: "bb"

s = "a"
print(solution.longestPalindrome(s))    # Output: "a"

s = "ababa"
print(solution.longestPalindrome(s))    # Output: "ababa"

s = "defthj"
print(solution.longestPalindrome(s))    # Output: "d"

s = "abaktednnd"
print(solution.longestPalindrome(s))    # Output: "dnnd"