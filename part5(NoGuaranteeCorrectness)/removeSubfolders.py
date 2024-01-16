# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-15 15:10:19
# LastEditTime: 2024-01-15 15:51:33
# Description: 

from collections import defaultdict
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.index = -1

class Solution:
    def removeSubfolders(self, folder):
        root = Trie()
        for i, path in enumerate(folder):
            cur = root
            for c in path:
                cur = cur.children[c]
            cur.index = i
        return self.dfs(root, folder)
        
    def dfs(self, root, folder):
        # stack = [root]
        # ans = []
        # while stack:
        #     cur = stack.pop()
        #     if cur.index != -1:
        #         ans.append(folder[cur.index])
        #     else:
        #         for t in cur.children.values():
        #             stack.append(t)
        # return ans

        stack = [root]
        ans = []
        while stack:
            cur = stack.pop()
            if cur.index != -1: # end of path
                ans.append(folder[cur.index])
            for c, t in cur.children.items():
                if cur.index == -1 or c != '/':
                    stack.append(t)
        return ans

Solution().removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"])

    

        





