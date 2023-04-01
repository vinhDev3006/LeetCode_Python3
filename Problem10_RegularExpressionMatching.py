"""
Problem 10: Regular Expression Matching
URL: https://leetcode.com/problems/regular-expression-matching/
Runtime: 322 ms, Beat: 6.39% [BAD SOLUTION 😂]
Memory: 13.8 MB, Beat: 87.22%
Description:
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".
"""
import unittest
import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return re.match(fr"^{p}$", s) is not None


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.testCase1 = ("aa", "a")
        self.testCase2 = ("ab", ".*")

    def test_test_case_1(self):
        self.assertEqual(False, self.solution.isMatch(self.testCase1[0], self.testCase1[1]))

    def test_test_case_2(self):
        self.assertEqual(True, self.solution.isMatch(self.testCase2[0], self.testCase2[1]))


if __name__ == '__main__':
    unittest.main()
