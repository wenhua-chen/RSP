# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-29 12:57:33
# LastEditTime: 2023-12-29 16:37:59
# Description: inplace quick sort


def quick_sort(arr):
    def partition(l, r):
        i = j = l
        while i <= r:
            if arr[i] <= arr[r]:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
            i += 1
        return j-1
        
    def sort(l, r):
        if l < r:
            index = partition(l, r)
            sort(l, index-1)
            sort(index+1, r)
    
    sort(0, len(arr)-1)



arr = [12, 11, 13, 5, 6, 7]
print(arr)

quick_sort(arr)
print(arr)

