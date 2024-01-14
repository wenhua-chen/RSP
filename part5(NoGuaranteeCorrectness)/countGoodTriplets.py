# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-14 10:43:36
# LastEditTime: 2024-01-14 10:43:38
# Description: 

class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        cnt = 0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                for k in range(j, len(arr)):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        cnt += 1
        return cnt

Solution().countGoodTriplets([3,0,1,1,9,7],7,2,3)


