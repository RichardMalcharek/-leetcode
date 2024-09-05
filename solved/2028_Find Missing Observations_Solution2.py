# region Quest
#You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the observations went missing, and you only have the observations of m rolls. Fortunately, you have also calculated the average value of the n + m rolls.
#
#You are given an integer array rolls of length m where rolls[i] is the value of the ith observation. You are also given the two integers mean and n.
#
#Return an array of length n containing the missing observations such that the average value of the n + m rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists, return an empty array.
#
#The average value of a set of k numbers is the sum of the numbers divided by k.
#
#Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.
#
# 
#
#Example 1:
#
#Input: rolls = [3,2,4,3], mean = 4, n = 2
#Output: [6,6]
#Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
#Example 2:
#
#Input: rolls = [1,5,6], mean = 3, n = 4
#Output: [2,3,2,2]
#Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
#Example 3:
#
#Input: rolls = [1,2,3,4], mean = 6, n = 4
#Output: []
#Explanation: It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
# endregion



### Time Limit Exceeded

from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        length = len(rolls) + n
        target = (mean * length)-sum(rolls)
        candidate = [(target//n) for _ in range(n)]

        if target > n*6 or target < n*1:
            return []
        try:
            while True:
                if sum(candidate) == target:
                    return candidate
                if sum(candidate) < target:
                    candidate[0] += 1
                    for x in range(0,len(candidate)):
                        if candidate[x] > 6:
                            candidate[x] = target//n
                            candidate[x+1] += 1
                if sum(candidate) > target:
                    candidate[0] -= 1
                    for x in range(0,len(candidate)):
                        if candidate[x] < 1:
                            candidate[x] = target//n
                            candidate[x+1] -= 1
        except:
            return []
    

solution = Solution()

rolls = [6,3,4,3,5,3]
mean = 1
n = 6
print(solution.missingRolls(rolls, mean, n))  # Output: []

rolls = [3,2,4,3]
mean = 4
n = 2
print(solution.missingRolls(rolls, mean, n))  # Output: [6,6]

rolls = [1,5,6]
mean = 3
n = 4
print(solution.missingRolls(rolls, mean, n))  # Output: [2,3,2,2]

rolls = [1,2,3,4]
mean = 6
n = 4
print(solution.missingRolls(rolls, mean, n)) # Output: []

rolls = [1,3,6,4,1,2,1,5,5,4]
mean = 6
n = 10
print(solution.missingRolls(rolls, mean, n))  # Output: 