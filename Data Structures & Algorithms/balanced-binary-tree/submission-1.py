# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.checkDepth(root.left)
        right = self.checkDepth(root.right)
        if max(left, right) - min(left, right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    def checkDepth(self, node):
        if not node:
            return 0
        return 1 + max(self.checkDepth(node.left), self.checkDepth(node.right))
    