# region Quest
#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
#A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#Example 1:
#
#Input: digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#Example 2:
#
#Input: digits = ""
#Output: []
#Example 3:
#
#Input: digits = "2"
#Output: ["a","b","c"]
# endregion


from typing import List


# Constraints:
#   0 <= digits.length <= 4
#   digits[i] is a digit in the range ['2', '9'].

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
                }
        
        length = len(digits)

        if length == 0:
            return []
        if length == 1:
            return dict[digits[0]]
        if length == 2:
            return [x + y for x in dict[digits[0]] for y in dict[digits[1]]]
        if length == 3:
            return [x + y + z for x in dict[digits[0]] for y in dict[digits[1]] for z in dict[digits[2]]]
        if length == 4:
            return [x + y + z + v for x in dict[digits[0]] for y in dict[digits[1]] for z in dict[digits[2]] for v in dict[digits[3]]]
        


solution = Solution()

digits = "23"
print(solution.letterCombinations(digits))  #Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

digits = ""
print(solution.letterCombinations(digits))  #Output: []

digits = "2"
print(solution.letterCombinations(digits))  #Output: ["a","b","c"]

digits = "7979"
print(solution.letterCombinations(digits))  #Output:

digits = "9999"
print(solution.letterCombinations(digits))  #Output:
