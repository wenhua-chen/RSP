# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-08 16:21:23
# LastEditTime: 2024-02-08 16:26:55
# Description: 

class Solution:
    def compress(self, chars):
        i = 0
        j = 1
        while j < len(chars):
            while j < len(chars) and chars[j] == chars[j-1]:
                j += 1
            dist = str(j-i)
            chars[i] = chars[j-1]
            i += 1
            j += 1
            if dist != '1':
                for k in range(len(dist)):
                    chars[i] = dist[k]
                    i += 1
        chars = chars[:i+1]
        return i+1

Solution().compress(["a","a","b","b","c","c","c"])

