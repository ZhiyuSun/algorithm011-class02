# 153. 寻找旋转排序数组中的最小值
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        if nums[right] > nums[0]:
            return nums[0]
        while left <= right: 
            mid = (left + right) // 2 
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1