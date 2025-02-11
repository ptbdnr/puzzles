"""Portorder traverse n-ary tree.

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = None, children: list["Node"] = None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: "Node") -> list[int]:
        self.l = []
        self.dfs(root)
        return self.l

    def dfs(self, n: "Node"):
        if n is None:
            return
        for c in n.children:
            self.dfs(c)
        self.l.append(n.val)
