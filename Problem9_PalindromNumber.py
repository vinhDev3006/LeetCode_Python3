"""Problem 9: Palindrome Number URL: https://leetcode.com/problems/palindrome-number/ Description: Given an integer
x, the task is to determine whether it is a palindrome or not. A palindrome is a number that remains the same when
its digits are reversed.

For example, the number 121 is a palindrome because it reads the same from left to right and from right to left. On
the other hand, the number -121 is not a palindrome because when read from left to right, it yields -121,
but when read from right to left, it becomes 121-. Therefore, it is not a palindrome. Similarly, the number 10 is not
a palindrome because it reads 01 from right to left, which is not the same as the original number.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        num_str = str(x)
        reversed_str = num_str[::-1]
        reversed_num = int(reversed_str)
        return x == reversed_num


solution = Solution()
print(solution.isPalindrome(-1234))
print(solution.isPalindrome(1234))
print(solution.isPalindrome(23232))
