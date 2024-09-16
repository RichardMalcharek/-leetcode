# region Quest
#Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
#
#Example 1:
#
#Input: timePoints = ["23:59","00:00"]
#Output: 1
#Example 2:
#
#Input: timePoints = ["00:00","23:59","00:00"]
#Output: 0
# 
#
#Constraints:
#
#2 <= timePoints.length <= 2 * 104
#timePoints[i] is in the format "HH:MM".
# endregion

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        timePoints_minutes = [int(time[:time.find(':')])*60+int(time[time.find(':')+1:]) for time in sorted(timePoints)]

        result = 1440 - timePoints_minutes[len(timePoints_minutes)-1] + timePoints_minutes[0]
 
        for i in range(1, len(timePoints_minutes)):
            difference = abs(timePoints_minutes[i] - timePoints_minutes[i-1])
            result = min(result, difference)
            if result == 0:
                break
        return result
    

solution = Solution()

timePoints = ["01:01","02:01"]
print(solution.findMinDifference(timePoints))   # Output: 60

timePoints = ["23:59","00:00"]
print(solution.findMinDifference(timePoints))   # Output: 1


timePoints = ["00:00","23:59","00:00"]
print(solution.findMinDifference(timePoints))   # Output: 0

timePoints = ["00:00","23:59","00:00","01:45","12:15"]
print(solution.findMinDifference(timePoints))   # Output: 0