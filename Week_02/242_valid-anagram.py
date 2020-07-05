# 242. 有效字母的异位词
# https://leetcode-cn.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        data = {}
        for i in s:
            if i in data:
                data[i] += 1
            else:
                data[i] = 1
        for i in t:
            if not i in data:
                return False
            data[i] -= 1
        for i in data.values():
            if i != 0:
                return False
        return True