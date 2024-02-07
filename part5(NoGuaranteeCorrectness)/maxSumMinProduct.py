# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-07 15:37:42
# LastEditTime: 2024-02-07 18:33:58
# Description: 

class Solution:
    def maxSumMinProduct(self, nums):
        nums = [0] + nums + [0]
        n = len(nums)
        
        p = [0]*(n+1)
        for i in range(n):
            p[i+1] = p[i] + nums[i]

        ans = 0
        mod = 10**9+7
        stack = []
        for i in range(n):
            while stack and nums[i] < nums[stack[-1]]:
                min_v = nums[stack.pop()]
                sub_sum = min_v * (p[i] - p[stack[-1]+1])
                ans = max(ans, sub_sum)
            stack.append(i)
        return ans % mod


    def maxSumMinProduct_method2(self, nums):
        # init left and right bdrs for each subarray
        n = len(nums)
        left = list(range(n))
        right = list(range(n))

        # determine left bdrs
        stack = []
        for i in range(n):
            while stack and nums[i] <= nums[stack[-1]]:
                left[i] = left[stack.pop()]
            stack.append(i)
        
        # determine right bdrs
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[i] <= nums[stack[-1]]:
                right[i] = right[stack.pop()]
            stack.append(i)
        
        # cal sum of previous i value for each i
        print(left)
        print(right)
        p = [0] * (n+1)
        for i in range(n):
            p[i+1] = p[i] + nums[i]

        # iterate all subarrays and find the max min_product
        ans = 0
        mod = 10**9+7
        for i in range(n):
            product = nums[i] * (p[right[i]+1]-p[left[i]])
            ans = max(ans, product)
        return ans % mod

Solution().maxSumMinProduct([1,2,3,2])