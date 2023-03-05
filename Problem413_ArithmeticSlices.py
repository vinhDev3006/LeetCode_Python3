"""
Problem 413: Arithmetic Slices
URL: https://leetcode.com/problems/fizz-buzz
Runtime: 39ms, Beats 90,35%
Memory: 15MB, Beats 33,31%
Description:
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzOrBuzz = ("Fizz", "Buzz", "FizzBuzz")
        return [fizzOrBuzz[2] if item % 15 == 0 else fizzOrBuzz[0] if item % 3 == 0 else fizzOrBuzz[
            1] if item % 5 == 0 else str(item) for item in range(1, n + 1)]

solution = Solution()
print(solution.fizzBuzz(15))

#['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
