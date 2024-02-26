# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-17 11:11:39
# LastEditTime: 2024-02-24 21:35:49
# Description: 

class Solution:
    def meetingrooms(self, intervals):
        start = sorted([time[0] for time in intervals])
        end = sorted([time[1] for time in intervals])

        n = len(intervals)
        i = j = 0
        cnt = 0
        max_cnt = 0
        while i < n and j < n:
            if start[i] < end[j]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
                i += 1
            else:
                cnt -= 1
                j += 1
        return max_cnt

intervals = [[0,30],[5,10],[10,15]]
print(Solution().meetingrooms(intervals))
