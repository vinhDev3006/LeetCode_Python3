"""
Problem 744: Find the Smallest Letter Greater Than Target
URL: https://leetcode.com/problems/find-smallest-letter-greater-than-target
Runtime: 100 ms, Beat: 97,62%
Memory: 134.3 MB, Beat: 71.2%

Description:
You are given an array of characters letters that is sorted in non-decreasing order,
and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target.
If such a character does not exist, return the first character in letters..

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
"""
import bisect
import unittest
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index = bisect.bisect_right(letters, target)
        return letters[0] if index >= len(letters) else letters[index]


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.testCase1 = (["c", "f", "k"], "d")
        self.testCase2 = (["x", "x", "y", "y"], "z")
        self.testCase3 = (["c", "f", "k"], "a")

    def test_test_case_1(self):
        self.assertEqual("f", self.solution.nextGreatestLetter(self.testCase1[0], self.testCase1[1]))

    def test_test_case_2(self):
        self.assertEqual("x", self.solution.nextGreatestLetter(self.testCase2[0], self.testCase2[1]))

    def test_test_case_3(self):
        self.assertEqual("c", self.solution.nextGreatestLetter(self.testCase3[0], self.testCase3[1]))


if __name__ == '__main__':
    unittest.main()
