# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-29 12:59:10
# LastEditTime: 2023-12-29 21:53:17
# Description: 

# arr must by sorted
def binary_search(arr, value):
    def find(l, r):
        if l > r:
            return -1
        mid = l + (r-l)//2
        if value == arr[mid]:
            return mid
        if value < arr[mid]:
            return find(l, mid-1)
        return find(mid+1, r)
    
    return find(0, len(arr)-1)

arr = [2, 3, 4, 10, 40]
x = 10
print(binary_search(arr, x))