# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-09 17:54:51
# LastEditTime: 2024-01-09 23:01:00
# Description: 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root):
        def helper(root, value):
            if root is None:
                return 0
            root.val += helper(root.right, 0) + value
            if root.left is None:
                return root.val
            return helper(root.left, root.val)

        helper(root, 0)
        return root

root = TreeNode(4, right=TreeNode(6, left=TreeNode(5), right= TreeNode(7, right= TreeNode(8))))
Solution().bstToGst(root)
