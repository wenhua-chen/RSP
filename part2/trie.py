# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-30 11:20:59
# LastEditTime: 2023-12-30 12:20:05
# Description: Trie insert, delete, search functions

class TrieNode:
    def __init__(self, char) -> None:
        self.char = char
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode(' ')
    
    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(char)
            cur = cur.children[char]
        cur.count += 1

    def search(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.count>0

    def delete(self, word):
        def helper(cur, word):
            if len(word) == 0:
                if cur.count > 0:
                    cur.count -= 1
                if (cur.count == 0) and (len(cur.children) == 0):
                    return None

            char = word[0]
            cur.children[char] = helper(cur.children[char], word[1:])
            
            cur.children = {k:v for k, v in cur.children.items() if v!=None}
            if len(cur.children) == 0:
                return None
            return cur
        
        self.root = helper(self.root, word)
    
    def traverse(self):
        def helper(cur, prev):
            for _ in range(cur.count):
                print(prev, end=' ')
            for char, node in cur.children.items():
                helper(node, prev+char)

        helper(self.root, '')
        print()

mytrie = Trie()
mytrie.insert('hello')
mytrie.insert('hell')
mytrie.insert('world')
mytrie.insert('word')
mytrie.traverse()

print(mytrie.search('world'))
mytrie.delete('world')
mytrie.traverse()

print(mytrie.search('hell'))
print(mytrie.search('hel'))
print(mytrie.search('helo'))
print(mytrie.search('world'))