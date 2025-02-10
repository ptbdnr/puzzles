"""Preorder Travers N-ary Tree.

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
"""

from typing import Optional

class Node:
    # Definition for a Node.
    def __init__(self, val: Optional[int] = None, children: Optional[list["Node"]] = None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: "Node") -> list[int]:
        self.preord = []
        self.dsf(root)
        return self.preord

    def dsf(self, n: "Node") -> None:
        if n is None:
            return
        self.preord.append(n.val)
        for c in n.children:
            self.dsf(c)
