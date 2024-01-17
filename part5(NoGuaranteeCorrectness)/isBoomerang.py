# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-17 11:39:22
# LastEditTime: 2024-01-17 12:02:18
# Description: 

class Solution:
    def isBoomerang1(self, points):
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        
        slope12 = (y2-y1)/(x2-x1) if x1 != x2 else 90
        slope13 = (y3-y1)/(x3-x1) if x1 != x3 else 90
        slope23 = (y3-y2)/(x3-x2) if x2 != x3 else 90

        slopes = set()
        slopes.add(slope12)
        slopes.add(slope13)
        slopes.add(slope23)
        return len(slopes) == 3
        

        

        if points[0][0] == points[1][0]:
            return points[2][0] != points[0][0]
        
        a = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
        b = points[1][1] - a*points[1][0]

        return points[2][1] != a*points[2][0] + b

    def isBoomerang2(self, points) -> bool:
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        x3, y3 = points[2][0], points[2][1]
        # slope between 1 and 2
        slope12 = 0
        if x2 - x1 == 0:
            slope12 = 90
        else:
            slope12 = (y2 - y1) / (x2 - x1)
            
        # slope between 1 and 3
        slope13 = 0
        if x3 - x1 == 0:
            slope13 = 90
        else:
            slope13 = (y3 - y1) / (x3 - x1)
            
        # slope between 2 and 3
        slope23 = 0
        if x3 - x2 == 0:
            slope23 = 90
        else:
            slope23 = (y3 - y2) / (x3 - x2)

        if slope12 == slope13 or slope12 == slope23 or slope13 == slope23:
            return False
        return True

Solution().isBoomerang1([[22,33],[37,27],[67,15]])

