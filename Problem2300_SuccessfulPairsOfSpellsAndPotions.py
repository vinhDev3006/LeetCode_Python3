"""
Problem 2300: Successful Pairs of Spells and Potions
URL: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
Runtime: 1273 ms, Beat: 83.57%
Memory: 37.2 MB, Beat: 50.42%
Description:
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents
the strength of the ith spell and potions[j] represents the strength of the jth potion. You are also given an integer
success. A spell and potion pair is considered successful if the product of their strengths is at least success. Return
an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair
with the ith spell.

Example:
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

💡Using binary search
"""
import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        potions_length = len(potions)
        ans = []
        for spell in spells:
            ans.append(potions_length - bisect_left(potions, success/spell))
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.testCase1 = ([5,1,3],[2,1,3,4,5],7)

    def test_test_case_1(self):
        self.assertEqual([4, 0, 3], self.solution.successfulPairs([5,1,3],[2,1,3,4,5],7))


if __name__ == '__main__':
    unittest.main()
