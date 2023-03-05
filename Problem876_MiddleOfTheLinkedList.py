"""
Problem 876: Middle of the Linked List
URL: https://leetcode.com/problems/middle-of-the-linked-list
Runtime: 39ms, Beats: 23,28%
Memory: 13.8MB, Beats 45.92%

Description:
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example:
Input: 1->2->3->4->5
Output: 3->4->5

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.val, end=" ")
            currentNode = currentNode.next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr = fast_ptr = head
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

a = ListNode(1)
b = ListNode(2); a.next = b
c = ListNode(3); b.next = c
d = ListNode(4); c.next = d
e = ListNode(5); d.next = e


solution = Solution()
myLinkedList = LinkedList(solution.middleNode(a))
myLinkedList.printLinkedList()