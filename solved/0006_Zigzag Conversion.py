# region Quest
#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
#
#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"
#
#Write the code that will take a string and make this conversion given a number of rows:
#
#string convert(string s, int numRows);
# 
#
#Example 1:
#
#Input: s = "PAYPALISHIRING", numRows = 3
#Output: "PAHNAPLSIIGYIR"
#Example 2:
#
#Input: s = "PAYPALISHIRING", numRows = 4
#Output: "PINALSIGYAHRPI"
#Explanation:
#P     I    N
#A   L S  I G
#Y A   H R
#P     I
#Example 3:
#
#Input: s = "A", numRows = 1
#Output: "A"
# endregion



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = []
        length = len(s)

        if numRows == 1:
            for i in range(length):
                result.append(s[i])
            return ''.join(result)
        
        width = numRows*2 - 2
        i = 0

        while i < numRows and i < length:
            position = i
            x = width - i*2
            y = abs(width - x)
            result.append(s[position])

            while position < length:
                position += x
                if x != 0 and position < length:
                    result.append(s[position])
                position += y
                if y != 0 and position < length:
                    result.append(s[position])
            i +=1
        
        return ''.join(result)


solution = Solution()


s = "PAYPALISHIRING"
numRows = 3
print(solution.convert(s,numRows))  # Output: " PAHNAPLSIIGYIR"
#                                               PAHNAPLSIIGYIR

s = "PAYPALISHIRING"
numRows = 4
print(solution.convert(s,numRows))  # Output: " PINALSIGYAHRPI"
#                                               PINALSIGYAHRPI

s = "A"
numRows = 1
print(solution.convert(s,numRows))  # Output: " A"