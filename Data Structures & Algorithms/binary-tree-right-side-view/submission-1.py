# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        self.checkDepth(root, 0, ans)
        return ans

    def checkDepth(self, node, level, ans):
        if not node:
            return
        if len(ans) == level:
            ans.append(node.val)
        self.checkDepth(node.right, level + 1, ans)
        self.checkDepth(node.left, level + 1, ans)
        
