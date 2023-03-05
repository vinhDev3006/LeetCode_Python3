"""
Problem 234: Palindrome Linked List
URL: https://leetcode.com/problems/palindrome-linked-list/
Description:
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1: 1 -> 2 -> 2 -> 1
True

Example 2: x -> y -> x
True

"""
from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        numbers = ""
        while head is not None:
            numbers += str(head.val)
            head = head.next
        rev_numbers = numbers[::-1]
        if numbers == rev_numbers:
            return True
        return False


a = ListNode(1)
b = ListNode(2); a.next = b
c = ListNode(2); b.next = c
d = ListNode(1); c.next = d

x = ListNode("x");
y = ListNode("y"); x.next = y
z = ListNode("x"); y.next = z



solution = Solution()
print(solution.isPalindrome(a)) #1221

print(solution.isPalindrome(x)) #xyx