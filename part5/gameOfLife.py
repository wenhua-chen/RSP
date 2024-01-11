# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-11 16:10:54
# LastEditTime: 2024-01-11 17:20:14
# Description: 


class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def sum_neighbour(i, j):
            res = 0
            for x in range(i-1, i+2):
                if x<0 or x>=m:
                    continue
                for y in range(j-1, j+2):
                    if y<0 or y>=n:
                        continue
                    if x == i and y == j:
                        continue
                    res += board[x][y]
            return res
        
        m = len(board)
        n = len(board[0])
        neighbour_sum = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                neighbour_sum[i][j] = sum_neighbour(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0 and neighbour_sum[i][j]==3:
                    board[i][j] = 1
                elif board[i][j] == 1 and (neighbour_sum[i][j] < 2 or neighbour_sum[i][j] > 3):
                    board[i][j] = 0
        
Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])

a = set()