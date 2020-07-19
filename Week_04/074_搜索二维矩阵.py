# 74. 搜索二维矩阵
# https://leetcode-cn.com/problems/search-a-2d-matrix/

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not (len(matrix) and len(matrix[0])):
            return False
        row, col = 0, len(matrix[0])-1
        while row <= len(matrix)-1 and col >= 0:
            curr = matrix[row][col]
            if curr == target: return True
            if target < curr:
                col -= 1
            else:
                row += 1
        return False