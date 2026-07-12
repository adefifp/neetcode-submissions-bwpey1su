# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)
        diam = left + right
        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(diam, sub)
    def getDepth(self, node):
        if not node:
            return 0
        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))