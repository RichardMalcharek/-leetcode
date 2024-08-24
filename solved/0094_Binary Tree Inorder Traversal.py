# region Quest
#Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
#Example 1:
#
#
#Input: root = [1,null,2,3]
#Output: [1,3,2]
#Example 2:
#
#Input: root = []
#Output: []
#Example 3:
#
#Input: root = [1]
#Output: [1]
# endregion


import time
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        List = []

        def inner(root):
            if not root:
                return
            
            inner(root.left)
            List.append(root.val)
            inner(root.right)
        
        inner(root)

        return List
        
    

solution = Solution()

root = [1, None, 2, 3]
print(solution.inorderTraversal(root)) #Output: [1,3,2]

root = []
print(solution.inorderTraversal(root)) #Output: []

root = [1]
print(solution.inorderTraversal(root)) #Output: [1]