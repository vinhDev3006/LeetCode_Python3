"""
Problem 1539: Kth Missing Positive Number
URL: https://leetcode.com/problems/kth-missing-positive-number
Runtime: 226ms, Beats: 6.31% [BAD SOLUTION 😂] 
Memory: 14MB, Beats: 44.89%
Description:
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.


Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

"""
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lNum = arr[-1]
        full_list = range(lNum + k + 1)
        result = [x for x in full_list if x not in arr]
        return result[k]


solution = Solution()
print(solution.findKthPositive([2, 3, 4, 7, 11], 5)) #9
