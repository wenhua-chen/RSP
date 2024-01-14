# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-12 16:06:19
# LastEditTime: 2024-01-12 16:26:50
# Description: 

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [1]
        opt = list(range(9,0,-1))
        opt.insert(0,9)
        opt.append(1)
        for i in range(n):
            opt[i] *= opt[i-1]
            dp.append(dp[-1] + opt[i])
        return dp[n]

print(Solution().countNumbersWithUniqueDigits(3))

