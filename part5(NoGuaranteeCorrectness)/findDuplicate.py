# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-25 15:09:09
# LastEditTime: 2024-01-25 15:12:54
# Description: 

class Solution:
    def findDuplicate(self, nums) -> int:
        l, r = 1, len(nums)-1
        while l < r:
            mid = l + (r-l)//2

            cnt = 0
            for n in nums:
                if n <= mid:
                    cnt += 1

            if cnt <= mid:
                l = mid+1
            else:
                r = mid
        return l

Solution().findDuplicate([1,3,4,2,2])

