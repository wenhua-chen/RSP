# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-03 16:25:54
# LastEditTime: 2023-12-28 17:16:53
# Description: 

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def height_update(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def left_rotate(self, x):
        y = x.right
        leaf = y.left
        # rotate
        x.right = leaf
        y.left = x
        # height
        self.height_update(x)
        self.height_update(y)
        return y

    def right_rotate(self, x):
        y = x.left
        leaf = y.right
        # rotate
        x.left = leaf
        y.right = x
        # height
        self.height_update(x)
        self.height_update(y)
        return y

    def insert(self, root, key):
        # normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        # height & balance factor
        self.height_update(root)
        balance = self.get_balance(root)

        # make balance
        if balance > 1:
            if key >= root.left.val:
                root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1:
            if key < root.right.val:
                root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif key > root.val:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                min_node = self.get_min(root.right)
                root.val = min_node.val
                root.right = self.delete(root.right, key)
        
        # height & balance factor
        self.height_update(root)
        balance = self.get_height(root.left) - self.get_height(root.right)
        
        # make balance
        if balance > 1:
            if self.get_balance(root.left) < 0:
                root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1:
            if self.get_balance(root.right) > 0:
                root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
        return root
            
    def get_min(self, node):
        if node is None or node.left is None:
            return node
        return self.get_min(node.left)

    # 前序
    def pre_order(self, node):
        if not node:
            return
        print(f'{node.val} ', end='')
        self.pre_order(node.left)
        self.pre_order(node.right)
    
    # 中序
    def in_order(self, node):
        if not node:
            return
        self.in_order(node.left)
        print(f'{node.val} ', end='')
        self.in_order(node.right)
    

myTree = AVLTree()

# test insert
root = None
root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25) 
myTree.pre_order(root)

# test delete
root = myTree.delete(root, 40)
root = myTree.delete(root, 10)
root = myTree.delete(root, 50)
myTree.pre_order(root)





















