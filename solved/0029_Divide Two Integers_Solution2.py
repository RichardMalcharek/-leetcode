# region Quest
#Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
#The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
#Return the quotient after dividing dividend by divisor.
#Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
#
#Example 1:
#
#Input: dividend = 10, divisor = 3
#Output: 3
#Explanation: 10/3 = 3.33333.. which is truncated to 3.
#
#Example 2:
#
#Input: dividend = 7, divisor = -3
#Output: -2
#Explanation: 7/-3 = -2.33333.. which is truncated to -2.
# 
#
#Constraints:
#
#-231 <= dividend, divisor <= 231 - 1
#divisor != 0
# endregion



# NOT / * %
# only int 
# range: -231 <= dividend, divisor <= 231 - 1

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = ''
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            result = result + '-' 

        num = 0
        count = 0

        if abs(divisor) == 1:
            result = int(result + str(abs(dividend)))
        else:
            result = int(result + str(len(range(0,abs(dividend)-abs(divisor)+1,abs(divisor)))))

        if result < -2**31:
            result = -2**31
        if result > 2**31-1:
            result = (2**31)-1
        return result

solution = Solution()


dividend = -2147483648
divisor = -1
Output = 2147483647
result = solution.divide(dividend, divisor)
print(f'{result==Output} : {result}')

dividend = 10
divisor = 3
Output = 3
result = solution.divide(dividend, divisor)
print(f'{result==Output} : {result}')

dividend = 7
divisor = -3
Output = -2
result = solution.divide(dividend, divisor)
print(f'{result==Output} : {result}')

dividend = -2147483648
divisor = -3
Output = 715827882
result = solution.divide(dividend, divisor)
print(f'{result==Output} : {result}')