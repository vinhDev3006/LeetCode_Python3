"""
Problem 1154: Day of the Year
URL: https://leetcode.com/problems/day-of-the-year/
Runtime: 62 ms, Beat: 93.88%
Memory: 13.9 MB, Beat: 62.45%

Description:
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Example 2:
Input: date = "2019-02-10"
Output: 41



"""
import unittest


class Solution:
    def dayOfYear(self, date: str) -> int:
        days_month = [31, 28, 31, 30, 31, 30, 31, 31 ,30, 31, 30, 31]
        year, month, day = map(int, date.split("-"))
        is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        sum = 0
        if month == 1:
            return day
        else:
            for i in range(0, month-1):
                sum += days_month[i]
            sum += day
        return sum + 1 if is_leap and month >= 3 else sum


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()
        self.testCase1 = "2019-01-09"
        self.testCase2 = "2019-02-10"

    def test_test_case_1(self):
        self.assertEqual(9, self.s.dayOfYear(self.testCase1))

    def test_test_case_2(self):
        self.assertEqual(41, self.s.dayOfYear(self.testCase2))


if __name__ == "__main__":
    unittest.main()

