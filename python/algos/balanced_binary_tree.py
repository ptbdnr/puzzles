"""Given a binary tree, determine if it is height-balanced.

Example:
Input: root = [random.randint(-10**4, 10**4) for _ in range(random.randint(0, 5000))]
Output: true|false

"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def isBalanced(node):
            if not node:
                return True
            return abs(height(node.left) - height(node.right)) <= 1 and isBalanced(node.left) and isBalanced(node.right)

        return isBalanced(root)
