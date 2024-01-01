# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-31 12:29:15
# LastEditTime: 2023-12-31 18:50:29
# Description: Prim with/without Heap in MST


# complexity: O(V^2), traverse all V distances for each Vertice
def prim_slow(graph, s):
    distance = [float('inf')] * len(graph)
    inTree = [False] * len(graph)
    parents = list(range(len(graph)))

    cur = s
    while inTree[cur] == False:
        inTree[cur] = True
        
        # update distace arr
        for k, v in graph[cur].items():
            if (inTree[k] == False) and (v < distance[k]):
                distance[k] = v
                parents[k] = cur
        # find min distance node
        for j in range(len(graph)):
            min_value = float('inf')
            if (inTree[j] == False) and (distance[j] < min_value):
                cur = j
    return parents

# faster using PriorityQueue, complexity: O(V*logV)
import heapq
def prim_fast(graph, s):
    distance = [float('inf')] * len(graph)
    inTree = [False] * len(graph)
    parents = list(range(len(graph)))
    pq = []

    cur = s
    while inTree[cur] == False:
        inTree[cur] = True
        
        # update distace arr
        for k, v in graph[cur].items():
            if (inTree[k] == False) and (v < distance[k]):
                heapq.heappush(pq, (v, k))
                distance[k] = v
                parents[k] = cur
        # find min distance node using heap
        cur = heapq.heappop(pq)[1]
    return parents

def print_mst(graph, parents):
    for i in range(len(graph)):
        if parents[i] != i:
            print(f'{i} - {parents[i]}: {graph[i][parents[i]]}')
        

graph = [
    {2:12, 3:7, 4:5},
    {6:2, 5:5},
    {0:12,3:4,6:7},
    {0:7,2:4,6:3,5:4,4:9},
    {0:5,3:9,5:7},
    {1:5,6:2,3:4,4:7},
    {1:2,5:2,3:3,2:7}
]

if __name__ == "__main__":
    parents = prim_slow(graph, 0)
    # parents = prim_fast(graph, 0)
    print_mst(graph, parents)
