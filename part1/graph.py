# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-19 23:19:44
# LastEditTime: 2023-12-22 12:03:19
# Description: Unweighted Graph

class EdgeNode:
    def __init__(self, y) -> None:
        self.y = y
        self.next = None

class Graph:
    def __init__(self, nvertices) -> None:
        self.edgeNode = [None] * nvertices
        self.degree = [0] * nvertices
        self.nvertices = nvertices
        self.nedges = 0
    
    def insert_edge(self, x, y, is_directed):
        p = EdgeNode(y)
        p.next = self.edgeNode[x]
        self.edgeNode[x] = p
        self.degree[x] += 1
        if not is_directed:
            self.insert_edge(y, x, True)
        else:
            self.nedges += 1
    
    def print_graph(self):
        for i in range(self.nvertices):
            print(f'{i}:', end='')
            node = self.edgeNode[i]
            while node:
                print(f' {node.y}', end='')
                node = node.next
            print()

myGraph = Graph(3)
myGraph.insert_edge(0,1,False)
myGraph.insert_edge(1,2,False)
myGraph.insert_edge(0,2,False)

myGraph.print_graph()

