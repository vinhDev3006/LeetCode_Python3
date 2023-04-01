"""
Problem 217: Contains Duplicate
URL: https://leetcode.com/problems/contains-duplicate
Runtime: 543 ms, Beat: 92.71%
Memory: 28.7 MB, Beat: 79.36%
Description:
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.


Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false
"""
import unittest
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.testCase1 = [1,2,3,1]
        self.testCase2 = [1,2,3,4]

    def test_test_case_1(self):
        self.assertEqual(True, self.solution.containsDuplicate(self.testCase1))

    def test_test_case_2(self):
        self.assertEqual(False, self.solution.containsDuplicate(self.testCase2))


if __name__ == '__main__':
    unittest.main()
