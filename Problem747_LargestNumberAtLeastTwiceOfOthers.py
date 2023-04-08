"""
Problem 747: Largest Number At Least Twice of Others
URL: https://leetcode.com/problems/largest-number-at-least-twice-of-others
Runtime: 29 ms, Beat: 94.75%
Memory: 13.8 MB, Beat: 47.8%

Description:
You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, or return -1 otherwise.

Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.

Example 2:
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
"""
import unittest
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        return nums.index(sorted_nums[0]) if sorted_nums[0] >= 2 * sorted_nums[1] else -1


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.testCase1 = [3,6,1,0]
        self.testCase2 = [1,2,3,4]

    def test_test_case_1(self):
        self.assertEqual(1, self.solution.dominantIndex(self.testCase1))

    def test_test_case_2(self):
        self.assertEqual(-1, self.solution.dominantIndex(self.testCase2))


if __name__ == '__main__':
    unittest.main()
