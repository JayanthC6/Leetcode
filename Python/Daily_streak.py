# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Problem: Sum of Root To Leaf Binary Numbers
'''Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0'''
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node,current_val):
            if not node:
                return 0
            current_val=(current_val<<1) | node.val
            if not node.left and not node.right:
                return current_val
            return dfs(node.left,current_val) + dfs(node.right,current_val)
        return dfs(root,0)           