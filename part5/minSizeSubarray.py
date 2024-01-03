# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-02 15:15:04
# LastEditTime: 2024-01-03 17:22:37
# Description: 

class Solution:
  def minSizeSubarray(self, nums, target) -> int:
    s = sum(nums)
    num_cycles, target = target // s, target % s

    seen, curr, res = {0: -1}, 0, float('inf')
    for i in range(len(nums) * 2):
      curr += nums[i % len(nums)]
      seen[curr] = i
      if curr - target in seen:
        res = min(res, i - seen[curr - target])

    res += num_cycles * len(nums)
    return -1 if res == float('inf') else res

nums = [1,1,1,2,3]

Solution().minSizeSubarray(nums, 8)