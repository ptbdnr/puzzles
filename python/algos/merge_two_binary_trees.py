"""Merge Two Binary Trees.

You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.
You need to merge the two trees into a new binary tree. 

The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.
Note: The merging process must start from the root nodes of both trees.
"""

class TreeNode:
    def __init__(self, val=0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode = None, root2: TreeNode = None) -> TreeNode:
        if root1 and root2:
            root_new = TreeNode(val = root1.val + root2.val)
            root_new.left = self.mergeTrees(root1.left, root2.left)
            root_new.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            root_new = root1
        elif root2:
            root_new = root2
        else:
            root_new = None
        return root_new
