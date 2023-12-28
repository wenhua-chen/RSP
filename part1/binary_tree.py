# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-19 23:19:32
# LastEditTime: 2023-12-20 18:33:11
# Description: 

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
    def __str__(self, level=0) -> str:
        ret = '\t'*level + repr(self.data) + '\n'
        if self.left:
            ret += self.left.__str__(level+1)
        if self.right:
            ret += self.right.__str__(level+1)
        return ret

class BinaryTree:

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                node = TreeNode(data)
                node.parent = self
                self.left = node
        else:
            if self.right:
                self.right.insert(data)
            else:
                node = TreeNode(data)
                node.parent = self
                self.right = node

    def search(self, data):
        if data == self.data:
            return self
        if data < self.data and self.left:
            return self.left.search(data)
        if data > self.data and self.right:
            return self.right.search(data)

    def traverse(self):
        if self.left:
            self.left.traverse()
        print(self.data)
        if self.right:
            self.right.traverse()

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self.data

    def delete(self, data):
        # 分情况讨论, 0/1/2个子节点, 如果有2个子节点, 需要找到successor, 然后替换, 再把successor删除
        pass


    
root = TreeNode(5)
root.insert(3)
root.insert(7)
root.insert(4)
print(root.search(1))

