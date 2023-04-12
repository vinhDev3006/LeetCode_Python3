"""
Problem 258: Add Digits
URL: https://leetcode.com/problems/add-digits
Runtime: 36 ms, Beat: 47.33%
Memory: 13.7 MB, Beat: 91.45%

Description:
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.


Example 2:
Input: num = 999999
Output: 9
Explanation: The process is
999999 --> 9 + 9 + 9 + 9 + 9 + 9--> 54
54 --> 5 + 4 --> 9
Since 9 has only one digit, return it.
"""
import unittest

class Solution:
    def addDigits(self, num: int) -> int:
        num_list = [int(d) for d in str(num)]
        if len(num_list) == 1:
            return num_list[0]
        else:
            return self.addDigits(sum(num_list))


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        self.testCase1 = 38
        self.testCase2 = 999999

    def test_test_case_1(self):
        self.assertEqual(2, self.s.addDigits(self.testCase1))

    def test_test_case2(self):
        self.assertEqual(9, self.s.addDigits(self.testCase2))

if __name__ == '__main__':
    unittest.main()