# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-15 16:21:05
# LastEditTime: 2024-01-15 16:40:42
# Description: 

from collections import defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges, blueEdges):
        red_dots = defaultdict(list)
        blue_dots = defaultdict(list)
        for n1, n2 in redEdges:
            red_dots[n1].append(n2)
        for n1, n2, in blueEdges:
            blue_dots[n1].append(n2)
        dots = [red_dots, blue_dots]

        q = [(0,0,0),(0,0,1)]
        seen = set()
        dist = [-1]*n
        dist[0] = 0
        for cur, steps, color in q:
            seen.add((cur, color))
            for node in dots[color][cur]:
                if (node, 1-color) not in seen:
                    q.append((node, steps+1, 1-color))
                    if dist[node] == -1:
                        dist[node] = steps+1
        return dist

            
Solution().shortestAlternatingPaths(3,[[0,1]],[[1,2]])



