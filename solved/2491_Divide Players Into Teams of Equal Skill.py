
from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        Sum_skill = sum(skill)
        length = len(skill)
        
        Team_skill = int((Sum_skill/length)*2)


        skill.sort()
        result = 0
        for i in range(0,length//2):
            Player1, Player2 = skill[i], skill[length-1-i]
            if Player1+Player2 != Team_skill:
                return -1
            result += (Player1*Player2)
        return result
            


solution = Solution()

skill = [2,3,4,2,5,5]
Output = 32
result = solution.dividePlayers(skill)
print(f'{result==Output} : {result}')


skill = [3,2,5,1,3,4]
Output = 22
result = solution.dividePlayers(skill)
print(f'{result==Output} : {result}')


skill = [3,4]
Output = 12
result = solution.dividePlayers(skill)
print(f'{result==Output} : {result}')

skill = [1,1,2,3]
Output = -1
result = solution.dividePlayers(skill)
print(f'{result==Output} : {result}')