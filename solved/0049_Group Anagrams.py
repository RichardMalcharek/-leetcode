# region Quest
#Given an array of strings strs, group the 
#anagrams
# together. You can return the answer in any order.
#
#Example 1:
#
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
#Explanation:
#
#There is no string in strs that can be rearranged to form "bat".
#The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
#The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
#Example 2:
#
#Input: strs = [""]
#
#Output: [[""]]
#
#Example 3:
#
#Input: strs = ["a"]
#
#Output: [["a"]]
#
# 
#
#Constraints:
#
#1 <= strs.length <= 104
#0 <= strs[i].length <= 100
#strs[i] consists of lowercase English letters.
# endregion


import time
from typing import Optional, List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        result = []
        pointer = 0

        for word in strs:
            curr = ''.join(sorted(word))
            if curr not in dict:
                dict[curr] = pointer
                pointer += 1
                result.append([word])
            else:
                index = dict[curr]
                result[index].append(word)
        
        return result




    

solution = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
Output = [["bat"],["nat","tan"],["ate","eat","tea"]]
result = solution.groupAnagrams(strs)
print(f'{result==Output} : {result}')

strs = [""]
Output = [[""]]
result = solution.groupAnagrams(strs)
print(f'{result==Output} : {result}')

strs = ["a"]
Output = [["a"]]
result = solution.groupAnagrams(strs)
print(f'{result==Output} : {result}')