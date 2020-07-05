# 1. 两数之和
# https://leetcode-cn.com/problems/two-sum/description/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data_dict = dict()
        for i, element in enumerate(nums):
            if target - element in data_dict:
                return [data_dict[target-element], i]
            data_dict[element] = i