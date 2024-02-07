# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-07 11:44:24
# LastEditTime: 2024-02-07 17:47:19
# Description: 

class Solution:
    def validSubarraySize(self, nums, threshold):
        nums = [0] + nums + [0]
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < nums[stack[-1]]:
                min_v = nums[stack.pop()]
                size = i - stack[-1] - 1
                if min_v > threshold/size:
                    return size
            stack.append(i)
        return -1

    
# Solution().validSubarraySize([1,3,4,3,1], 6)
Solution().validSubarraySize([6,5,6,5,8], 7)