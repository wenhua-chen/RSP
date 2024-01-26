# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-26 10:07:03
# LastEditTime: 2024-01-26 10:07:04
# Description: 


def compare_trees(root1, root2):
  def pre_traverse(root):
    # if root is a leaf, append it to arr
    if not root.left and not root.right:
      arr.append(root.val)
  	# else traverse its left and right nodes
    if root.left:
      pre_traverse(root.left)
    if root.right:
      pre_traverse(root.right)

  # traverse root1
  arr = []
  pre_traverse(root1)
  
  # traverse root2
  arr1 = arr.copy()
  arr = []
  pre_traverse(root2)
  return arr1 == arr


def find_val(root):
  def dfs(node, max_val, min_val):
    # reset max_val and min_val if needed
    if node.val > max_val:
      max_val = node.val
    if node.val < min_val:
      min_val = node.val
    
    # abs cal
    val = max(abs(max_val-node.val), abs(min_val-node.val))
    
    # dfs left and right
    if node.left:
      val = max(val, dfs(node.left, max_val, min_val))
    if node.right:
      val = max(val, dfs(node.right, max_val, min_val))
    return val
  
  return dfs(root, root.val, root.val)