"""
Exercise 28: Find The Index of the First Occurrence in a String
URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string
Runtime: 33 ms, Beat: 50.5%
Memory: 13.7 MB, Beat: 94.77%
Description:
Given two strings needle and haystack, return the index of the first occurrence of
needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""
import unittest
import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = re.search(needle, haystack)
        return -1 if not match else match.start()


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.testCase1 = ("sadbutsad", "sad")
        self.testCase2 = ("leetcode", "leeto")
        self.testCase3 = ("hello", "ll")

    def test_test_case_1(self):
        self.assertEqual(0, self.solution.strStr(self.testCase1[0], self.testCase1[1]))

    def test_test_case_2(self):
        self.assertEqual(-1, self.solution.strStr(self.testCase2[0], self.testCase2[1]))

    def test_test_case_3(self):
        self.assertEqual(2, self.solution.strStr(self.testCase3[0], self.testCase3[1]))


if __name__ == '__main__':
    unittest.main()
