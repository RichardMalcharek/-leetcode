# region Quest
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# 
#
#Example 1:
#
#Input: x = 123
#Output: 321
#Example 2:
#
#Input: x = -123
#Output: -321
#Example 3:
#
#Input: x = 120
#Output: 21
# endregion




class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            revX = int(str(x*-1)[::-1])*-1
            if revX < -2**31 or revX > 2**31 -1:
                return 0
            return revX
        else:
            revX = int(str(x)[::-1])
            if revX < -2**31 or revX > 2**31 -1:
                return 0
            return revX

solution = Solution()

x = 123
print(solution.reverse(x))  # Output: 321
x = -123
print(solution.reverse(x))  # Output: -321
x = 120
print(solution.reverse(x))  # Output: 21

x = -2_147_483_648
print(solution.reverse(x))  # Output: 0
x = 2_147_483_647
print(solution.reverse(x))  # Output: 0

x = 7_463_847_412
print(solution.reverse(x))  # Output: 2_147_483_647
x = 8_463_847_412
print(solution.reverse(x))  # Output: 0
x = -8_463_847_412
print(solution.reverse(x))  # Output: -2_147_483_648
x = -9_463_847_412
print(solution.reverse(x))  # Output: 0