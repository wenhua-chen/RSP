# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-05 12:19:15
# LastEditTime: 2024-02-05 15:25:20
# Description: 

class UF:
    def __init__(self, n):
        self.p = list(range(n))
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

from collections import defaultdict
class Solution:
    def smallestStringWithSwaps_uf(self, s: str, pairs) -> str:
        # find all connections
        uf = UF(len(s))
        for x,y in pairs:
            uf.union(x,y)
        connections = defaultdict(list)
        for i in range(len(s)):
            connections[uf.find(i)].append(i)

        # in each connection, sort index according to their value
        result = [None] * len(s)
        for con in connections.values():
            index_sort = sorted(con)
            value_sort = sorted(con, key=lambda i: s[i])
            for i, v in zip(index_sort, value_sort):
                result[i] = s[v]
        return ''.join(result)

    def smallestStringWithSwaps_dfs(self, s: str, pairs) -> str:
        # in dfs, add all met vertices to seens and current connection
        def dfs(node):
            c.append(node)
            seens.add(node)
            for n in al[node]:
                if n not in seens:
                    dfs(n)

        # init adjacency list, seens and current connection and connections
        al = [[] for _ in range(len(s))]
        for x, y in pairs:
            al[x].append(y)
            al[y].append(x)
        seens = set()
        
        # iterate through s, if i is not in seens, update connection, perform dfs
        # sort each connection by i and s[i], then add to ans
        ans = [None] * len(s)
        for i in range(len(s)):
            if i not in seens:
                c = []
                dfs(i)
                for x, y in zip(sorted(c), sorted(c, key=lambda i: s[i])):
                    ans[x] = s[y]
        return ans

print(Solution().smallestStringWithSwaps_dfs(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))
