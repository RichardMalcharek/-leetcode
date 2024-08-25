# region Quest
#Given a string s, find the length of the longest 
#substring
# without repeating characters.
#
# 
#
#Example 1:
#
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:
#
#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:
#
#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# endregion


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxR = len(set(s))
        if maxR<= 1:
            return maxR
        result = 0
        i = 0
        j = 0
        while i + result < len(s) and result < maxR:
            sub = s[i:j+1]
            if len(set(sub)) == len(sub):
                result = max(result, len(sub))
                j += 1
            else:
                i += 1
                j = i +result
    
        return result

solution = Solution()


s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s)) #Output: 3

s = "bbbbb"
print(solution.lengthOfLongestSubstring(s)) #Output: 1

s = "pwwkew"
print(solution.lengthOfLongestSubstring(s)) #Output: 3

s = "dvdf"
print(solution.lengthOfLongestSubstring(s)) #Output: 3