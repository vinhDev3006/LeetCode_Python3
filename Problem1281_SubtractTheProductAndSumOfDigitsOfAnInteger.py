"""
Problem 258: Add Digits
URL: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer
Runtime: 30 ms, Beat: 71.23%
Memory: 13.8 MB, Beat: 91.31%

Description:
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
"""
import unittest
import math


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num_list = [int(d) for d in str(n)]
        return math.prod(num_list) - sum(num_list)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        self.testCase1 = 234
        self.testCase2 = 4421

    def test_test_case_1(self):
        self.assertEqual(15, self.s.subtractProductAndSum(self.testCase1))

    def test_test_case2(self):
        self.assertEqual(21, self.s.subtractProductAndSum(self.testCase2))


if __name__ == '__main__':
    unittest.main()
