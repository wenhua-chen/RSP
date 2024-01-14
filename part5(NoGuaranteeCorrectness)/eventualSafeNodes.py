# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-03 23:37:59
# LastEditTime: 2024-01-06 15:36:46
# Description: 

class Solution:
    def eventualSafeNodes(self, graph):
        def is_safe(cur):
            if safe_nodes[cur] != None:
                return safe_nodes[cur]
            if seens[cur] == 1:
                safe_nodes[cur] = 0
                return False
            seens[cur] = 1
            for node in graph[cur]:
                if (node==cur) or (not is_safe(node)):
                    safe_nodes[cur] = 0
                    return False
            safe_nodes[cur] = 1
            return True
        
        # find loops
        safe_nodes = [None] * len(graph)
        seens = [0] * len(graph)
        for i in range(len(graph)):
            if safe_nodes[i] == None:
                is_safe(i)
        return [i for i in range(len(graph)) if safe_nodes[i]==1]


# graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# graph = [[],[0,2,3,4],[3],[4],[]]
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Solution().eventualSafeNodes(graph)