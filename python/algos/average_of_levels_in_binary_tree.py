"""Compute average of levels in binary tree.

Given the root of a binary tree, 
return the average value of the nodes on each level in the form of an array. 
Answers within 10-5 of the actual answer will be accepted.
"""

from collections import deque


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val: int =0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode = None) -> list[float]:
        if root is None:
            return []

        c, res = 1, []
        q = deque([root])
        while len(q):
            nodes = [q.pop() for _ in range(c)]
            vals = [n.val for n in nodes if n]
            if len(vals):
                res.append(sum(vals) / len(vals))
            c = 0
            for n in nodes:
                if n:
                    q.append(n.left)
                    q.append(n.right)
                    c += 2
        return res
