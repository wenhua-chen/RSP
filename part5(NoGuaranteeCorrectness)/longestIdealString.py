# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-27 12:51:52
# LastEditTime: 2024-01-27 12:51:54
# Description: 

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*26
        for c in s:
            ind = ord('c') - ord('a')
            dp[ind] = max(dp[max(0,ind-k):ind+k+1]) + 1
        return max(dp)
    
Solution().longestIdealString('acfgbd',2)

