# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-12 17:27:58
# LastEditTime: 2024-01-13 18:57:29
# Description: 

class Solution:
    def combinationSum4(self, nums, target):
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i>=num:
                    dp[i] += dp[i-num]
        return dp[target]

print(Solution().combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10))