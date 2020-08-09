from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def _generate(left, right, n, s):
            if left == n and right == n:
                res.append(s)
                return
            
            if left < n:
                _generate(left+1, right, n, s+"(")

            if left > right:
                _generate(left, right+1, n, s+")")

        
        res = []
        _generate(0, 0, n, "")
        return res