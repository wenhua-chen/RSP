# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-19 23:01:40
# LastEditTime: 2024-01-19 23:01:42
# Description: 

class Solution:
    def coinChange(self, coins, amount) -> int:
        coins.sort()
        cnt = 0
        for coin in coins[::-1]:
            cnt += amount // coin
            amount = amount % coin
            if (amount==0):
                break
        return cnt if amount == 0 else -1

Solution().coinChange([186,419,83,408], 6249)