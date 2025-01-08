from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            is_leaf = not any([root.left, root.right])
            return self.helper(root, is_leaf, 0, targetSum)
        return False

    def helper(self, n: Optional[TreeNode], is_leaf: bool, curr: int, target: int) -> bool:
        if n is None:
            return curr == target and is_leaf
        curr += n.val
        is_leaf = not any([n.left, n.right])
        return self.helper(n.left, is_leaf, curr, target) or self.helper(n.right, is_leaf, curr, target)
