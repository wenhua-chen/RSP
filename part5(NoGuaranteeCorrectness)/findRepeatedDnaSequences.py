# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-25 17:28:00
# LastEditTime: 2024-01-25 17:29:39
# Description: 

class Solution:
    def findRepeatedDnaSequences(self, s: str):
        seens = set()
        i = 10
        ans = set()
        while i <= len(s):
            sub = s[i-10:i]
            if sub in seens:
                ans.add(sub)
            else:
                seens.add(sub)
            i += 1
        return list(ans)

Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
