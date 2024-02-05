# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-26 20:39:27
# LastEditTime: 2024-02-06 09:57:17
# Description: 


class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # total = 0
        # for i in range(7,0,-1):
        #     mod = k**i
        #     if n > mod:
        #         total += n // mod
        #         n %= mod
        # return total
        sum = 0
        while n > 0:
            sum += n % k
            n = n // k
        return sum
    

print(Solution().sumBase(25, 3))
