# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-19 23:19:22
# LastEditTime: 2023-12-20 17:53:20
# Description: 

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return str(self.data)

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def __str__(self) -> str:
        result = []
        node = self.head
        while node:
            result.append(str(node))
            node = node.next
        return ' '.join(result)
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return node
            node = node.next

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    node.next = node.next.next
                    break
                node = node.next
                
linkedlist = LinkedList()
linkedlist.insert(5)
linkedlist.insert(4)
linkedlist.insert(3)
linkedlist.insert(2)
linkedlist.insert(1)
print(linkedlist)

print(linkedlist.search(4))

linkedlist.delete(6)
print(linkedlist)


    
