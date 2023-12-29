# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-19 23:20:38
# LastEditTime: 2023-12-29 12:53:02
# Description: 

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * len(self.graph)
        queue = []
        queue.append(s)
        visited[s] = True
        while len(queue) > 0:
            cur = queue.pop(0)
            print(cur, end=' ')
            for index in self.graph[cur]:
                if visited[index] == False:
                    queue.append(index)
                    visited[index] = True

    def DFS(self, s):
        def DFS_Helper(cur):
            print(cur, end=' ')
            for index in self.graph[cur]:
                if visited[index] == False:
                    visited[index] = True
                    DFS_Helper(index)
        
        visited = [False] * len(self.graph)
        visited[s] = True
        DFS_Helper(s)

if __name__ == '__main__':

    # Test BFS
    # g = Graph()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 0)
    # g.addEdge(1, 3)
    # g.addEdge(2, 0)
    # g.addEdge(2, 4)
    # g.addEdge(3, 1)
    # g.addEdge(3, 4)
    # g.addEdge(4, 3)
    # g.addEdge(4, 2)
    # g.BFS(0)

    # Test DFS
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 0)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 0)
    g.addEdge(3, 2)
    g.addEdge(4, 2)
    g.DFS(0)
