"""
Problem 12: Integer to Roman
URL: https://leetcode.com/problems/integer-to-roman
Runtime: 43 ms, Beat: 89.81%
Memory: 13.8 MB, Beat: 67.5%

Description:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply
X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
import unittest



class Solution:
    def intToRoman(self, num: int) -> str:
        if num >= 1000: return 'M' + self.intToRoman(num - 1000)
        if num >= 900: return 'CM' + self.intToRoman(num - 900)
        if num >= 500: return 'D' + self.intToRoman(num - 500)
        if num >= 400: return 'CD' + self.intToRoman(num - 400)
        if num >= 100: return 'C' + self.intToRoman(num - 100)
        if num >= 90: return 'XC' + self.intToRoman(num - 90)
        if num >= 50: return 'L' + self.intToRoman(num - 50)
        if num >= 40: return 'XL' + self.intToRoman(num - 40)
        if num >= 10: return 'X' + self.intToRoman(num - 10)
        if num >= 9: return 'IX' + self.intToRoman(num - 9)
        if num >= 5: return 'V' + self.intToRoman(num - 5)
        if num >= 4: return 'IV' + self.intToRoman(num - 4)
        if num >= 1: return 'I' + self.intToRoman(num - 1)
        return ""


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.testCase1 = 1994
        self.testCase2 = 3724

    def test_test_case_1(self):
        self.assertEqual('MCMXCIV', self.solution.intToRoman(self.testCase1))

    def test_test_case_2(self):
        self.assertEqual('MMMDCCXXIV', self.solution.intToRoman(self.testCase2))


if __name__ == '__main__':
    unittest.main()
