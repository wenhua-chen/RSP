# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-29 12:57:26
# LastEditTime: 2023-12-29 15:48:08
# Description: create new arr_L and arr_R, merge back to original arr

def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    arr_L = arr[:mid]
    arr_R = arr[mid:]
    merge_sort(arr_L)
    merge_sort(arr_R)
    
    # inplace merge, no return
    i = j = k = 0
    while i < len(arr_L) and j < len(arr_R):
        if arr_L[i] < arr_R[j]:
            arr[k] = arr_L[i]
            i += 1
        else:
            arr[k] = arr_R[j]
            j += 1
        k += 1
    while i < len(arr_L):
        arr[k] = arr_L[i]
        i += 1
        k += 1
    while j < len(arr_R):
        arr[k] = arr_R[j]
        j += 1
        k += 1
    

arr = [12, 11, 13, 5, 6, 7]
print(arr)

merge_sort(arr)
print(arr)