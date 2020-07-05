# 429: N叉树的层序遍历
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from typing import List

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        result = []
        previous_layer = [root]
        while previous_layer:
            result.append([])
            current_layer = []
            for node in previous_layer:
                result[-1].append(node.val)
                current_layer.extend(node.children)
            previous_layer = current_layer
        return result