# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-21 10:40:00
# LastEditTime: 2023-12-21 11:04:14
# Description: 

class TrieNode:
    def __init__(self, char) -> None:
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode('')
    
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        node.is_end = True
        node.counter += 1
    
    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix+node.char, node.counter))
        else:
            for child in node.children.values():
                self.dfs(child, prefix+node.char)

    def query(self, prefix):
        self.output = []
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        
        self.dfs(node, prefix[:-1])
