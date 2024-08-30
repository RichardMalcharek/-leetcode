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

import time

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max2 = sorted(height, reverse=True)
        maxVolume = 0
        
        for i in range(0,len(height)-1):
            for j in range(len(height)-1,i,-1):
                value = min(height[i],height[j]) * (j-i)
                maxVolume = max(value, maxVolume)     
                if maxVolume >= (max2[1]) * (j-i-1):
                    break
            if maxVolume >= (max2[1]) * (len(height)-i-1):
                break
        return maxVolume

solution = Solution()

start_time = time.time()
tries = 100_000
for x in range(tries):
    height = [2,3,4,5,18,17,6]
    solution.maxArea(height)     # Output: 17
    height = [1,8,6,2,5,4,8,3,7]
    solution.maxArea(height)     # Output: 49
    height = [1,1]
    solution.maxArea(height)     # Output: 1
    height = [76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191]
    solution.maxArea(height)     # Output: 18048

end_time = time.time()
timesum = end_time - start_time
print(f' benötigte Zeit: {timesum}')

