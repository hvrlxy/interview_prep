'''
Given the root of a binary tree, return the level order 
traversal of its nodes' values. (i.e., from left to 
right, level by level).
'''

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # create a list to store the results
        res = []
        # check if the root is empty
        if not root:
            return res
        
        # perform an iterative preorder traversal
        stack = deque()
        stack.append((root, 0))
        while len(stack) > 0:
            node, level = stack.pop()
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
            
            # if the level is not in the list, add it
            while len(res) <= level:
                res.append([])
                
            # add the value to the appropriate list
            res[level].append(node.val)
            
        return res
        