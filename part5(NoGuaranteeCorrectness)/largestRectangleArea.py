# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-07 16:44:47
# LastEditTime: 2024-02-07 18:20:07
# Description: 

class Solution:
    def largestRectangleArea(self, heights):
        heights = [0] + heights + [0]
        stack = []
        ans = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                print(height, heights[stack[-1]+1:i])
                ans = max(ans, height*(i-stack[-1]-1))
            stack.append(i)
        return ans

    def largestRectangleArea_method2(self, heights):
        n = len(heights)
        left = list(range(n))
        right = list(range(n))

        stack = []
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                left[i] = left[stack.pop()]
            stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[i] <= heights[stack[-1]]:
                right[i] = right[stack.pop()]
            stack.append(i)
        
        ans = 0
        for i in range(n):
            ans = max(ans, (right[i] - left[i]+1) * heights[i])
        return ans

Solution().largestRectangleArea([2,1,5,5,6,2,3])

