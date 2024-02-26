# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-24 21:17:36
# LastEditTime: 2024-02-24 21:21:47
# Description: 

import numpy as np
class Solution:
    def spiralOrder(self, matrix):
        m, n = len(matrix), len(matrix[0])
        matrix = np.array(matrix)
        l, r = 0, n-1
        t, b = 0, m-1

        res = []
        while l<r and t<b:
            res.extend(matrix[t,l:r])
            res.extend(matrix[t:b,r])
            res.extend(matrix[b,r:l:-1])
            res.extend(matrix[b:t:-1,l])
            t, l, b, r = t+1, l+1, b-1, r-1
        if t == b and l == r:
            res.append(matrix[t][l])
        else:
            if t == b:
                res.extend(matrix[t][l:r+1])
            if l == r:
                res.extend(matrix[t:b+1][r])
        return res

res = Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(res)