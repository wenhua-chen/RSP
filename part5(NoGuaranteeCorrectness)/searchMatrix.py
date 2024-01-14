# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-11 12:12:17
# LastEditTime: 2024-01-11 12:40:38
# Description: 

class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            l, r = 0, n-1
            while l <= r:
                mid = l + (r-l)//2
                if target == mid:
                    return True
                if target < mid:
                    r = mid - 1
                else:
                    l = mid + 1
        return False

matrix = [[ 1, 2, 3, 4, 5],
          [ 6, 7, 8, 9,10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]]

Solution().searchMatrix(matrix, 15)

