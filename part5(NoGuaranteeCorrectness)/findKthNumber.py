# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-27 11:06:24
# LastEditTime: 2024-01-27 11:08:53
# Description: 

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # return int(sorted(map(str, range(1,n+1)))[k-1])
        def partition(l,r):
            i = j = l
            pivot = str(arr[r])
            while i <= r:
                if str(arr[i]) <= pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    j += 1
                i += 1
            return j-1
        
        def find(l, r):
            cur = partition(l, r)
            if cur == k:
                return arr[k]
            if cur < k:
                return find(cur+1, r)
            else:
                return find(l, cur-1)
        
        k -= 1
        arr = list(range(1,n+1))
        return find(0, n-1)
        
print(Solution().findKthNumber(1,1))

