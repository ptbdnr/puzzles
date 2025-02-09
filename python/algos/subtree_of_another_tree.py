"""Define if subtree.

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootOrder, subOrder = [], []
        self.order(root, rootOrder)
        self.order(subRoot, subOrder)
        nr, ns = len(rootOrder), len(subOrder)
        for ri, rv in enumerate(rootOrder):
            if ri + ns <= nr and rootOrder[ri:ri+ns] == subOrder:
                return True
        return False
    
    def order(self, n: TreeNode, l: list) -> None:
        l.append(n.val if n else None)
        if n is None:
            return
        self.order(n.left, l)
        self.order(n.right, l)
