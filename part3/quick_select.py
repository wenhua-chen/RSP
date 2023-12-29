# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-29 12:59:01
# LastEditTime: 2023-12-29 17:03:02
# Description: quick select k_th value

def quick_select(arr, k):
    def partition(l, r):
        i = j = l
        while i <= r:
            if arr[i] <= arr[r]:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
            i += 1
        return j-1

    def find(l, r):
        cur = partition(l, r)
        if cur == k:
            return arr[cur]
        elif cur < k:
            return find(cur+1, r)
        return find(l, cur-1)
    
    if 0 <= k and k < len(arr):
        return find(0, len(arr)-1)


arr = [12, 11, 13, 5, 6, 7]
for k in range(len(arr)):
    print(quick_select(arr, k))