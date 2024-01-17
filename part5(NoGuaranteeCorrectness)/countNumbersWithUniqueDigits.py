# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-12 16:06:19
# LastEditTime: 2024-01-17 09:47:57
# Description: 

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        dp = [1]
        dig_cnt = 9
        for i in range(n):
            dp.append(dp[-1]+dig_cnt)
            dig_cnt *= 9-i
        return dp[-1]

print(Solution().countNumbersWithUniqueDigits(2))

