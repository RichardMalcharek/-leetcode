# region Quest
#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
#Example 1:
#
#Input: haystack = "sadbutsad", needle = "sad"
#Output: 0
#Explanation: "sad" occurs at index 0 and 6.
#The first occurrence is at index 0, so we return 0.
#Example 2:
#
#Input: haystack = "leetcode", needle = "leeto"
#Output: -1
#Explanation: "leeto" did not occur in "leetcode", so we return -1.
# endregion


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        x = len(needle)
        for i in range(0,len(haystack)-x+1):
            if haystack[i:i+x] == needle:
                return i
        return -1



solution = Solution()

haystack = "sadbutsad"
needle = "sad"
print(solution.strStr(haystack, needle))

haystack = "leetcode"
needle = "leeto"
print(solution.strStr(haystack, needle))