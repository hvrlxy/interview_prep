'''
Given the root of a binary tree, determine if it 
is a valid binary search tree (BST).

A valid BST is defined as follows:

    - The left subtree of a node contains only 
    nodes with keys less than the node's key.
    - The right subtree of a node contains only 
    nodes with keys greater than the node's key.
    - Both the left and right subtrees must 
    also be binary search trees.
'''
import numpy as np
from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # check if the root is empty
        if not root:
            return True
        
        # perform an iterative preorder traversal with min-max range included
        stack = deque()
        stack.append((root, -np.inf, np.inf))
        while (len(stack) > 0):
            node, node_min, node_max = stack.pop()
            # check if the node is valid
            if node.val >= node_max or node.val <= node_min:
                return False
            # add the right child if it exists, with the min-max range adjusted
            if node.right:
                stack.append((node.right, max(node_min, node.val), node_max))
            # add the left child if it exists, with the min-max range adjusted
            if node.left:
                stack.append((node.left,  node_min, min(node_max, node.val)))
                
        return True