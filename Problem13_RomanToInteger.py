"""
Problem13:Roman To Integer
URL: https://leetcode.com/problems/roman-to-integer/
Description:
Roman numerals are a number system that uses a combination of seven different symbols to represent values: I, V, X, L, C, D, and M. These symbols have corresponding values of 1, 5, 10, 50, 100, 500, and 1000.

To write numbers in Roman numerals, the symbols are usually written largest to smallest from left to right. However, there are six special cases where subtraction is used to represent numbers:

"IV" represents 4 (instead of IIII)
"IX" represents 9 (instead of VIIII)
"XL" represents 40 (instead of XXXX)
"XC" represents 90 (instead of LXXXX)
"CD" represents 400 (instead of CCCC)
"CM" represents 900 (instead of DCCCC)

Given a Roman numeral, the task is to convert it to an integer.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        list_special_cases = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        roman_value = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000
        }
        item_list = []
        for i in range(len(s) - 1):
            pair = s[i:i + 2]
            if pair in list_special_cases:
                item_list.append(pair)

        for r in item_list:
            s = s.replace(r, '')

        result = list(s) + item_list

        total_sum = 0
        for x in result:
            total_sum += roman_value[x]
        return total_sum


solution = Solution()
print(solution.romanToInt("MCMXCIV")) #1994
