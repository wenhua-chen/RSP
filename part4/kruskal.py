# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-31 18:53:04
# LastEditTime: 2024-01-01 12:46:11
# Description: complexity: O(E + V*logV)

from union_find import UnionFind
import heapq

def kruskal(graph):
    unionfind = UnionFind(len(graph))

    # construct edges minHeap
    edges = []
    for i in range(len(graph)):
        for k, v in graph[i].items():
            if k > i:
                heapq.heappush(edges, (v, k, i))
    
    # union components
    count = 1
    results = []
    while count < len(graph):
        w, i, j = heapq.heappop(edges)
        if not unionfind.same_component(i, j):
            count += 1
            unionfind.union(i, j)
            results.append((w, i, j))
    return results

def print_mst(results):
    for w, i, j in results:
        print(f'{i} - {j}: {w}')

graph = [
    {2:12, 3:7, 4:5},
    {6:2, 5:5},
    {0:12,3:4,6:7},
    {0:7,2:4,6:3,5:4,4:9},
    {0:5,3:9,5:7},
    {1:5,6:2,3:4,4:7},
    {1:2,5:2,3:3,2:7}
]

if __name__ == '__main__':

    results = kruskal(graph)
    print_mst(results)


