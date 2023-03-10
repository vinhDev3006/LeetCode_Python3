"""
Problem 1342: Number of Steps to Reduce a Number to Zero
URL: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero
Runtime: 31ms, Beats 74.73%
Memory: 13.9MB, Beats 43.22%

Description:
Given an integer num, return the number of steps to reduce it to zero. In one step, if the current number is even,
you have to divide it by 2, otherwise, you have to subtract 1 from it.

Example:
Input: num = 14
Output: 6

Explanation:
Step 1) 14 is even; divide by 2 and obtain 7.
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 5) 2 is even; divide by 2 and obtain 1.
Step 6) 1 is odd; subtract 1 and obtain 0.

"""
class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num != 0:
            num = num // 2 if num & 1 == 0 else num - 1
            counter += 1
        return counter


solution = Solution()
print(solution.numberOfSteps(123)) #12