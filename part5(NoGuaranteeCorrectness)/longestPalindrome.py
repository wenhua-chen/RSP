# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-02 16:10:40
# LastEditTime: 2024-02-02 16:12:39
# Description: 

class Solution:
    def longestPalindrome(self, s: str) -> str:
         # init
        n = len(s)
        ans = ''
        # iterate
        for i in range(n):
            for j in range(i, n):
                if s[i:j+1][::-1] in {s[i:j+1]} and (j+1-i) > len(ans): # s[i:j+1] is a palindrom
                    ans = s[i:j+1] # update seen
        return ans

Solution().longestPalindrome('babad')

