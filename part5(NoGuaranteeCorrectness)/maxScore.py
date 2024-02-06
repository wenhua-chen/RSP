# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-02-06 11:27:01
# LastEditTime: 2024-02-06 12:32:53
# Description: 

class Solution:
    def maxScore(self, nums, x):
        i = total = 0
        cur_par = nums[0]%2

        while i < len(nums):
            par_sum = nums[i]
            # add all values to par_sum until par(i) ! = par(i-1)
            while i+1 < len(nums) and nums[i+1]%2 == nums[i]%2:
                par_sum += nums[i+1]
                i += 1
            if nums[i]%2 == cur_par:
                total += par_sum
            else:
                if par_sum > x:
                    total += par_sum-x
                    cur_par = nums[i]%2
            i += 1
        return total

print(Solution().maxScore([38,92,23,30,25,96,6,71,78,77,33,23,71,48,87,77,53,28,6,20,90,83,42,21,64,95,84,29,22,21,33,36,53,51,85,25,80,56,71,69,5,21,4,84,28,16,65,7], 52))

