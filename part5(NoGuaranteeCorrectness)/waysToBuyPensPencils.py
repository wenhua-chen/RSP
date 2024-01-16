# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-15 17:06:22
# LastEditTime: 2024-01-15 17:06:24
# Description: 

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        total = 0
        for i in range(total//cost1 + 1):
            total += (total-i*cost1) //cost2 + 1
        return total

Solution().waysToBuyPensPencils(20, 10, 5)

