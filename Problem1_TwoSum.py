"""
Exercise 1: Two Sum 
URL: https://leetcode.com/problems/two-sum/
Description:
Given an array of integers 🧮 nums and an integer 🧮 target, find the indices of the two numbers in the array 📊 
that add up to the target 🎯. You may assume that each input would have exactly one solution and you may not use 
the same element twice. You can return the answer in any order 🔄.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIdx = {}
        for idx, num in enumerate(nums):
            rem = target - num
            if rem not in numToIdx:
                numToIdx[num] = idx
            else:
                return [numToIdx[rem],idx]

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3,2,4], 6))