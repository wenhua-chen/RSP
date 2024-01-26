# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-26 11:38:26
# LastEditTime: 2024-01-26 11:55:31
# Description: 

class Solution:
    def maxSum(self, nums, k: int) -> int:
        MOD = 10**9 + 7
        bits = [0] * 32
        for num in nums:
            for i in range(32):
                if (num & (1 << i)):
                    bits[i] += 1
        
        arr = []
        for _ in range(len(nums)):
            val = 0
            for i in range(32):
                if bits[i] > 0:
                    bits[i] -= 1
                    val |= (1 << i)
            arr.append(val)
        
        ans = 0
        for i in range(k):
            ans += arr[i]**2
            ans %= MOD
        return ans
    
Solution().maxSum([118,72,7], 2)