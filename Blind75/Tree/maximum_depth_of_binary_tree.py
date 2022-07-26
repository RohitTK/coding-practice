from typing import Optional

"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3


Example 2:

Input: root = [1,null,2]
Output: 2

"""


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        return self.traverse(height=0, root=root)

    def traverse(self, height, root):
        if not root:
            return height
        else:
            height = height + 1
            return max(self.traverse(height, root.left), self.traverse(height, root.right))

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left = self.maxDepth2(root.left)
            right = self.maxDepth2(root.right)
            return max(left, right) + 1

