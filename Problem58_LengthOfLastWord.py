"""
Exercise 58: Length of last word
URL: https://leetcode.com/problems/length-of-last-word
Runtime: 34 ms, Beat: 42.72%
Memory: 42.72 MB, Beat: 69.37%
Description:
Given a string s consisting of words and spaces, return the length of the last word in the string. A word is a maximal
substring consisting of non-space characters only.

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
"""
import unittest
import re


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(re.findall(r"\w+", s)[-1])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.testCase1 = "    fly me     to    the Moon  "
        self.testCase2 = "Hello World"

    def test_test_case_1(self):
        self.assertEqual(4, self.solution.lengthOfLastWord(self.testCase1))

    def test_test_case_2(self):
        self.assertEqual(5, self.solution.lengthOfLastWord(self.testCase2))


if __name__ == "__main__":
    unittest.main()
