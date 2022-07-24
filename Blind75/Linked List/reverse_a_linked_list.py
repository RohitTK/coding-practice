from typing import Optional

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
"""

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Logic: Iterative
    def iterativeReverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None

        while head:
            curr_node = head
            head = head.next
            curr_node.next = prev_node
            prev_node = curr_node

        return prev_node

    # Logic: Recursive
    def recursiveReverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursiveReverseListFn(head, None)

    def recursiveReverseListFn(self, node, prev_node):
        if not node:
            return prev_node
        n = node.next
        node.next = prev_node
        return self.recursiveReverseListFn(n, node)
