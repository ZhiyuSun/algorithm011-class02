# 455. 分发饼干
# https://leetcode-cn.com/problems/assign-cookies/

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
            g.sort()
            s.sort()
            count = 0
            j = 0
            for i in range(len(s)):
                if j < len(g) and s[i] >= g[j]:
                    count += 1
                    j += 1
            return count