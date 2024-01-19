# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-19 17:07:18
# LastEditTime: 2024-01-19 17:12:08
# Description: 

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        max_index = min(arrLen, steps//2+1)
        cur_ways = [0] * (max_index+2)
        cur_ways[1] = 1
        next_ways = [0] * (max_index+2)
        
        while steps > 0:
            for i in range(1, max_index+1):
                next_ways[i] = cur_ways[i] + cur_ways[i-1] + cur_ways[i+1]
            cur_ways, next_ways = next_ways, cur_ways
            steps -= 1
        return cur_ways[1]

Solution().numWays(3,2)

