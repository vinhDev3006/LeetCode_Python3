"""
Problem 4: Median of Two Sorted Arrays
URL: https://leetcode.com/problems/median-of-two-sorted-arrays
Runtime: 90 ms, Beat: 81.72%
Memory: 14.1 MB, Beat: 93.82%
Description:
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
import unittest
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergeList = sorted(nums1 + nums2)
        length = len(mergeList)
        mid = length // 2
        return mergeList[mid] if length % 2 == 1 else ((mergeList[mid-1] + mergeList[mid]) / 2)


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.testCase1 = ([1, 3], [2])
        self.testCase2 = ([1, 2], [3, 4])

    def test_test_case_1(self):
        self.assertEqual(2, self.solution.findMedianSortedArrays(self.testCase1[0], self.testCase1[1]))

    def test_test_case_2(self):
        self.assertEqual(2.5, self.solution.findMedianSortedArrays(self.testCase2[0], self.testCase2[1]))


if __name__ == '__main__':
    unittest.main()
