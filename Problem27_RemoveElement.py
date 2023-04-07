"""
Problem 27: Remove Element
URL: https://leetcode.com/problems/remove-element
Runtime: 26 ms, Beat: 97,17%
Memory: 13.8 MB, Beat: 49.46%

Description:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements
may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
import bisect
import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = list(filter(lambda x: x != val, nums))
        return len(nums)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.testCase1 = ([0,1,2,2,3,0,4,2], 2)

    def test_test_case_1(self):
        self.assertEqual(5, self.solution.removeElement(self.testCase1[0], self.testCase1[1]))


if __name__ == '__main__':
    unittest.main()
