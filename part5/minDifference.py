# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-04 11:34:06
# LastEditTime: 2024-01-09 12:30:27
# Description: 

class Solution:
    def minDifference(self, nums) -> int:
        nums.sort()
        return min(b-a for a,b in zip(nums[:4], nums[-4:]))

Solution().minDifference([3,100,20])