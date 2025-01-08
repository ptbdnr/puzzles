"""Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, n: TreeNode, lvl: int) -> int:
        if n is None:
            return lvl
        if n.left and n.right:
            return min(self.dfs(n.left, lvl+1), self.dfs(n.right, lvl+1))
        if n.left:
            return self.dfs(n.left, lvl+1)
        if n.right:
            return self.dfs(n.right, lvl+1)
        return lvl+1
