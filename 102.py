# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Time Complexity = O(n)
# space complexity = O(n) as we are using a queue
from collections import deque
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        
        return result
        