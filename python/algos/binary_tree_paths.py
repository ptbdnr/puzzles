"""Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.
"""

from __future__ import annotations


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: TreeNode=None, right: TreeNode=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        paths = []
        if root:
            self.helper(root, f"{root.val}", paths)
        return paths

    def helper(self, node: TreeNode, curr_path: str, paths: list[str]):
        if node is None:
            return
        if node.left is None and node.right is None:
            paths.append(curr_path)
            return

        for n in [node.left, node.right]:
            if n:
                new_path = f"{curr_path}->{n.val}"
                self.helper(n, new_path, paths)
