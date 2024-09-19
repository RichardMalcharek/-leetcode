# region Quest
#Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.
#The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed 104.
#
#Example 1:
#
#Input: expression = "2-1-1"
#Output: [0,2]
#Explanation:
#((2-1)-1) = 0 
#(2-(1-1)) = 2
#
# Example 2:
#
#Input: expression = "2*3-4*5"
#Output: [-34,-14,-10,-10,10]
#Explanation:
#(2*(3-(4*5))) = -34 
#((2*3)-(4*5)) = -14 
#((2*(3-4))*5) = -10 
#(2*((3-4)*5)) = -10 
#(((2*3)-4)*5) = 10
# 
#
#Constraints:
#
#1 <= expression.length <= 20
#expression consists of digits and the operator '+', '-', and '*'.
#All the integer values in the input expression are in the range [0, 99].
#The integer values in the input expression do not have a leading '-' or '+' denoting the sign.
# endregion


from typing import List

class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        def dfs(i, j):
            if i == j:
                return [int(s[i])]
            if i == j - 1 and s[j] not in '+-*':
                return [int(s[i: j + 1])]
            if (i, j) in memo:
                return memo[(i, j)]
            res = []
            for k in range(i, j + 1):
                ch = s[k]
                if ch in '+-*':
                    left = dfs(i, k - 1)
                    right = dfs(k + 1, j)
                    for l1 in left:
                        for l2 in right:
                            if ch == '+':
                                res += [l1 + l2]
                            elif ch == '-':
                                res += [l1 - l2]
                            elif ch == '*':
                                res += [l1 * l2]
            memo[(i, j)] = res
            return memo[(i, j)]
        n = len(s)
        memo = dict()
        return dfs(0, n - 1)



solution = Solution()

expression = "2-1-1"
Output = [0,2]
result = solution.diffWaysToCompute(expression)
print(f'{result==Output} : {result}')

expression = "2*3-4*5"
Output = [-34,-14,-10,-10,10]
result = solution.diffWaysToCompute(expression)
print(f'{result==Output} : {result}')