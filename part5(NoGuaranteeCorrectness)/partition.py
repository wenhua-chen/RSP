# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-25 11:52:54
# LastEditTime: 2024-01-25 12:20:51
# Description: 

class Solution:
    def partition(self, s: str):
        def dfs(new_s, cur_res):
            if not new_s:
                res.append(cur_res)
                return
            for i in range(len(new_s)):
                if new_s[:i+1] == new_s[:i+1][::-1]:
                    dfs(new_s[i+1:], cur_res+[new_s[:i+1]])
        
        res = []
        dfs(s, [])
        return res

Solution().partition("aab")
