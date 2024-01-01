# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-31 12:29:15
# LastEditTime: 2024-01-01 17:37:25
# Description: Dijkstra with/without Heap in MST


# complexity: O(V^2), traverse all V distances for each Vertice
def Dijkstra_slow(graph, s):
    distance = [float('inf')] * len(graph)
    inTree = [False] * len(graph)
    parents = list(range(len(graph)))

    cur = s
    distance[s] = 0
    while inTree[cur] == False:
        inTree[cur] = True
        
        # update distance arr
        for k, v in graph[cur].items():
            if (inTree[k] == False) and ((v+distance[cur]) < distance[k]):
                distance[k] = v+distance[cur]
                parents[k] = cur
        # find min distance node
        min_value = float('inf')
        for j in range(len(graph)):
            if (inTree[j] == False) and (distance[j] < min_value):
                cur = j
                min_value = distance[j]
    return parents, distance

# faster using PriorityQueue, complexity: O(V*logV)
import heapq
def Dijkstra_fast(graph, s):
    distance = [float('inf')] * len(graph)
    inTree = [False] * len(graph)
    parents = list(range(len(graph)))
    pq = []

    cur = s
    distance[s] = 0
    while inTree[cur] == False:
        inTree[cur] = True
        
        # update distance arr
        for k, v in graph[cur].items():
            if (inTree[k] == False) and (v+distance[cur] < distance[k]):
                heapq.heappush(pq, (v, k))
                distance[k] = v+distance[cur]
                parents[k] = cur
        # find min distance node using heap
        cur = heapq.heappop(pq)[1]
    return parents, distance

def print_path(parents, distance):
    def recursion(parents, cur, path):
        path.append(str(cur))
        if cur == parents[cur]:
            return
        else:
            recursion(parents, parents[cur], path)
    
    for i in range(len(graph)):
        if i != parents[i]:
            path = []
            recursion(parents, i, path)
            print(f'{" - ".join(path[::-1])}: {distance[i]}')
            

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
    # parents, distance = Dijkstra_slow(graph, 0)
    parents, distance = Dijkstra_fast(graph, 0)
    print_path(parents, distance)
