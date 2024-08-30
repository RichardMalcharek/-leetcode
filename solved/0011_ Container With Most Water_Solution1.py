# region Quest
#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
#Return the maximum amount of water a container can store.
#
#Notice that you may not slant the container.
# endregion

from typing import List

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        maxVolume = 0
        for i in range(0,length-1):
            for j in range(i+1,length):
                maxVolume = \
                    max(    
                        maxVolume,
                        (min(height[j],height[i])*(j-i))
                        )
        return maxVolume


    

solution = Solution()

height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height))     # Output: 49

height = [1,1]
print(solution.maxArea(height))     # Output: 1
