"""
Exercise 14: Longest Common PreFix
URL: https://leetcode.com/problems/longest-common-prefix
Runtime: 38 ms, Beats: 45.64% 
Memory: 13.9 MB, Beats: 78.53%
Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
"""
import unittest

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs = sorted(strs)
        first_w = strs[0]
        last_w = strs[-1]
        for i in range(min(len(first_w), len(last_w))):
            if first_w[i] != last_w[i]:
                return res
            res += first_w[i]
        return res


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.testCase1 = ["flower", "flow", "flight"]
        self.testCase2 = ["dog", "racecar", "car"]

    def test_test_case_1(self):
        self.assertIn('fl', self.solution.longestCommonPrefix(self.testCase1))

    def test_test_case_2(self):
        self.assertIn('', self.solution.longestCommonPrefix(self.testCase2))


if __name__ == "__main__":
    unittest.main()
