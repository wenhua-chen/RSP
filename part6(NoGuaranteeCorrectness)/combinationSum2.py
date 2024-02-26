# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-26 10:49:04
# LastEditTime: 2024-02-26 10:49:06
# Description: 

class Solution:
    def combinationSum2(self, candidates, target):
        def dfs(total, arr, i):
            if total == target:
                res.append(arr)
                return
            if i >= len(candidates) or total > target:
                return
            dfs(total, arr, i+1)
            dfs(total+candidates[i],arr+[candidates[i]], i+1)

        res = []
        dfs(0,[],0)
        return res
    
Solution().combinationSum2([10,1,2,7,6,1,5],8)

