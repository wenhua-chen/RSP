# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-06 10:42:28
# LastEditTime: 2024-02-06 10:42:31
# Description: 

class Solution:
    def addMinimum(self, word):
        # init total = 0
        total = 0
        # two pointers i,j
        i = 0
        # j start from i+1, increase j until ord(word[j])>ord(word[i]), add ij distance to total
        while i < len(word):
            j = i+1
            while j < len(word) and word[j] > word[j-1]:
                j += 1
            total += 3 - (j-i)
            i = j
        return total
    
print(Solution().addMinimum('aaaabb'))


