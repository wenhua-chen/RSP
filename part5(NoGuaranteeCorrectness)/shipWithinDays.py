# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-24 15:52:22
# LastEditTime: 2024-01-24 15:52:24
# Description: 

class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        def is_fit(cap):
            cnt = 1
            total = 0
            for weight in weights:
                total += weight
                if total > cap:
                    cnt += 1
                    total = weight
            return cnt <= days
        
        l, r = max(weights), sum(weights)
        while l<r:
            mid = l + (r-l)//2
            if is_fit(mid):
                r = mid
            else:
                l = mid+1
        return l

Solution().shipWithinDays([3,2,2,4,1,4],3)