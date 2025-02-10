"""Determine if subtree of another tree.

Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode = None, subRoot: TreeNode = None) -> bool:
        rootOrder, subOrder = [], []
        self.order(root, rootOrder)
        self.order(subRoot, subOrder)
        nr, ns = len(rootOrder), len(subOrder)
        return any(ri + ns <= nr and rootOrder[ri:ri + ns] == subOrder for ri in range(rootOrder))

    def order(self, n: TreeNode, l: list) -> None:
        if n is None:
            l.append(None)
            return
        l.append(n.val)
        self.order(n.left, l)
        self.order(n.right, l)
