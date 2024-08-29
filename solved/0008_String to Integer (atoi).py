# region Quest
#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
#
#The algorithm for myAtoi(string s) is as follows:
#
#Whitespace: Ignore any leading whitespace (" ").
#Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
#Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
#Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
#Return the integer as the final result.
#
# 
#
#Example 1:
#
#Input: s = "42"
#
#Output: 42
#
#Explanation:
#
#The underlined characters are what is read in and the caret is the current reader position.
#Step 1: "42" (no characters read because there is no leading whitespace)
#         ^
#Step 2: "42" (no characters read because there is neither a '-' nor '+')
#         ^
#Step 3: "42" ("42" is read in)
#           ^
#Example 2:
#
#Input: s = " -042"
#
#Output: -42
#
#Explanation:
#
#Step 1: "   -042" (leading whitespace is read and ignored)
#            ^
#Step 2: "   -042" ('-' is read, so the result should be negative)
#             ^
#Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
#               ^
#Example 3:
#
#Input: s = "1337c0d3"
#
#Output: 1337
#
#Explanation:
#
#Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#         ^
#Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#         ^
#Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#             ^
#Example 4:
#
#Input: s = "0-1"
#
#Output: 0
#
#Explanation:
#
#Step 1: "0-1" (no characters read because there is no leading whitespace)
#         ^
#Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
#         ^
#Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
#          ^
#Example 5:
#
#Input: s = "words and 987"
#
#Output: 0
##
#Explanation:
#
#Reading stops at the first non-digit character 'w'.
# endregion



class Solution:
    def myAtoi(self, s: str) -> int:
        stack = []
        length = len(s)
        pointer = 0
        nums = '0123456789'

        while pointer < length and s[pointer] == " ":
            pointer += 1
        
        if pointer < length and (s[pointer] == '-' or s[pointer] == '+'):
            stack.append(s[pointer])
            stack.append(0)
            pointer +=1

        while pointer < length and s[pointer] in nums:
            stack.append(s[pointer])
            pointer += 1
        
        if not stack:
            return 0

        result = ''.join(map(str, stack))
        result = int(result)

        if result < -2**31:
            return -2**31
        if result > 2**31 -1:
            return 2**31 -1
        return result


        

            

solution = Solution()

s = ""
print(solution.myAtoi(s))   #Output: 0

s = "42"
print(solution.myAtoi(s))   #Output: 42

s = " -042"
print(solution.myAtoi(s))   #Output: -42

s = "1337c0d3"
print(solution.myAtoi(s))   #Output: 1337

s = "0-1"
print(solution.myAtoi(s))   #Output: 0

s = "words and 987"
print(solution.myAtoi(s))   #Output: 0