# 347. 前 K 个高频元素
# https://leetcode-cn.com/problems/top-k-frequent-elements/

import collections, heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)   
        return heapq.nlargest(k, count.keys(), key=count.get)