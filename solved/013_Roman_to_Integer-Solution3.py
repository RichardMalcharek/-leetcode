# region Quest
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer.
#
# 
#
#Example 1:
#
#Input: s = "III"
#Output: 3
#Explanation: III = 3.
#Example 2:
#
#Input: s = "LVIII"
#Output: 58
#Explanation: L = 50, V= 5, III = 3.
#Example 3:
#
#Input: s = "MCMXCIV"
#Output: 1994
#Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# endregion

import time

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        while s != '':
            if len(s) >= 2:
                if s[0] == 'C' and s[0+1] == 'M':
                    result += 900
                    s = s[0+2:]
                    continue
                if s[0] == 'C' and s[0+1] == 'D':
                    result += 400
                    s = s[0+2:]
                    continue
                if s[0] == 'X' and s[0+1] == 'C':
                    result += 90
                    s = s[0+2:]
                    continue
                if s[0] == 'X' and s[0+1] == 'L':
                    result += 40
                    s = s[0+2:]
                    continue
                if s[0] == 'I' and s[0+1] == 'X':
                    result += 9
                    s = s[0+2:]
                    continue
                if s[0] == 'I' and s[0+1] == 'V':
                    result += 4
                    s = s[0+2:]
                    continue
            if s[0] == 'M':
                result += 1000
                s = s[0+1:]
                continue
            if s[0] == 'D':
                result += 500
                s = s[0+1:]
                continue
            if s[0] == 'C':
                result += 100
                s = s[0+1:]
                continue
            if s[0] == 'L':
                result += 50
                s = s[0+1:]
                continue
            if s[0] == 'X':
                result += 10
                s = s[0+1:]
                continue
            if s[0] == 'V':
                result += 5
                s = s[0+1:]
                continue
            if s[0] == 'I':
                result += 1
                s = s[0+1:]
                continue

        return result
    
solution = Solution()
timesum = 0
tries = 1_000_000

for x in range(tries):
    start_time = time.time()
    for rome in ['III', 'LVIII', 'MCMXCIV']: # = 3, 58 , 1994
        print(f'{solution.romanToInt(rome)}, ', end="")
    end_time = time.time()
    timesum += end_time - start_time

print()
print(f'average runtime: {format(round(timesum/tries,10),".10f")}')
# average runtime by 1.000.000 tries: 0.0001104263