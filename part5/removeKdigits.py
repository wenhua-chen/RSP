# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-09 12:44:11
# LastEditTime: 2024-01-09 16:35:49
# Description: 

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = []
        for n in num:
            while result and k and result[-1] > n:
                result.pop()
                k -= 1
            if result or n!='0':
                result.append(n)
        if k:
            result = result[:-k]
        return ''.join(result) or '0'
                

Solution().removeKdigits("1432219",3)

