# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-25 10:34:44
# LastEditTime: 2024-02-25 10:41:45
# Description: 

class Solution:
    def hIndex(self, citations):
        def is_valid(h):
            cnt = 0
            for c in citations:
                if c >= h:
                    cnt += 1
            return cnt>=h
        
        l, r = 0, len(citations)-1
        while l < r:
            mid = l + (r-l)//2
            if is_valid(mid):
                l = mid + 1
            else:
                r = mid
        
        return l-1 if l!=0 else 0

Solution().hIndex([1])