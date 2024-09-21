# region Quest
#Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
# You must write an algorithm that runs in O(n) time and uses O(1) extra space. 
#
#Example 1:
#
#Input: n = 13
#Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
#
#Example 2:
#
#Input: n = 2
#Output: [1,2]
# 
#
#Constraints:
#
#1 <= n <= 5 * 104
# endregion


from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        List = list(map(int, sorted([str(x) for x in range(1,n+1)])))
        return List
    

solution = Solution()


n = 13
Output = [1,10,11,12,13,2,3,4,5,6,7,8,9]
result = solution.lexicalOrder(n)
print(f'{result==Output} : {result}')

n = 2
Output = [1,2]
result = solution.lexicalOrder(n)
print(f'{result==Output} : {result}')