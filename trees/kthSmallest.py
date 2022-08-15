'''
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the 
values of the nodes in the tree.
'''

from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # create a list to store the values of the nodes of 
        # the tree in ascending order
        res = []
        
        # perform an iterative traversal of the tree
        stack = deque()
        stack.append(root)
        current = root
        while True:
            if (current):
                stack.append(current)
                current = current.left
            elif (stack):
                node = stack.pop()
                res.append(node.val)
                if len(res) == k:
                    return node.val
                current = node.right
            else:
                break
                
        return -1
                
        
        