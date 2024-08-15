# region Quest
#Write a function to find the longest common prefix string amongst an array of strings.
#
#If there is no common prefix, return an empty string "".
#
#Example 1:
#
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Example 2:
#
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
# endregion

import time
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        currentString = strs[0]
        for x in range(1,len(strs)):
            i = min(len(currentString), len(strs[x]))
            while True and i >=0:
                if currentString[:i] == strs[x][:i]:
                    currentString = currentString[:i]
                    break
                i -= 1
            if i == -1:
                return ""
        return currentString

solution = Solution()
timesum = 0
tries = 1
for x in range(tries):
    start_time = time.time()

    List = ["flower", "flow", "flight"]
    print(f'List: {List}')
    print(f'result: {solution.longestCommonPrefix(List)}')
    print()

    List = ["dog", "racecar", "car"]
    print(f'List: {List}')
    print(f'result: {solution.longestCommonPrefix(List)}')
    print()

    List = ["interstellar", "internet", "interval"]
    print(f'List: {List}')
    print(f'result: {solution.longestCommonPrefix(List)}')
    print()

    List = ["apple", "apricot", "banana"]
    print(f'List: {List}')
    print(f'result: {solution.longestCommonPrefix(List)}')
    print()

    end_time = time.time()
    timesum += end_time - start_time

print()
print(f'average runtime: {format(round(timesum/tries,10),".10f")}')
# average runtime by 1.000.000 tries: ....