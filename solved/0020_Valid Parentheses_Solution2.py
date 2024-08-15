# region Quest
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#An input string is valid if:
#
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Every close bracket has a corresponding open bracket of the same type.
# 
#
#Example 1:
#
#Input: s = "()"
#Output: true
#Example 2:
#
#Input: s = "()[]{}"
#Output: true
#Example 3:
#
#Input: s = "(]"
#Output: false
# endregion



## beats 67,70 %


import time

class Solution:
    def isValid(self, s: str) -> bool:
        closing = [')', ']', '}']
        opening = ['(', '[', '{']
        stack = []
        if len(s)%2 != 0:
            return False
        for digit in s:
            if digit in opening:
                stack.append(opening.index(digit))
                continue
            if len(stack) == 0 and digit in closing:
                return False
            if digit in closing and closing.index(digit) != stack[len(stack)-1]:
                return False
            if digit in closing and closing.index(digit) == stack[len(stack)-1]:
                stack.pop()
                continue 
        if len(stack) > 0:
            return False   
        return True
    

solution = Solution()
timesum = 0
tries = 1
for x in range(tries):
    start_time = time.time()

    s = "["        # False
    print(f'{s}', end='')
    print(solution.isValid(s))

    s = "[("        # False
    print(f'{s}', end='')
    print(solution.isValid(s))

    s = ")()"        # False
    print(f'{s}', end='')
    print(solution.isValid(s))

    s = "()"        # True
    print(f'{s}', end='')
    print(solution.isValid(s))

    s = "()[]{}"    # True
    print(f'{s}', end='')
    print(solution.isValid(s))

    s = "(]"        # True
    print(f'{s}', end='')
    print(solution.isValid(s))

    end_time = time.time()
    timesum += end_time - start_time

print()
print(f'average runtime: {format(round(timesum/tries,10),".10f")}')