# 55. 跳跃游戏
# https://leetcode-cn.com/problems/jump-game/

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        end_reachable = len(nums) - 1
        for i in range(len(nums)-1, -1 , -1):
            if nums[i] + i >= end_reachable:
                end_reachable = i
        return end_reachable == 0