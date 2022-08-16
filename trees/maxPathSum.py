'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
in the sequence has an edge connecting them. A node can only appear in the 
sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty 
path.
'''

'''
Algorithm:

We will do dynamic programming on three variables: maximum path including the root
and one of the subtrees (max_including_root), maximum path excluding the root, 
(max_excluding_root) and maximum path brigding the root with the left and right 
subtrees (max_bridge).

The recursion works as follows:
maxPathSum(root) = max(max_including_root, max_excluding_root, max_bridge)

maxPath(node):
    for node:
        if node is empty:
            max_including_root = -inf
            max_excluding_root = -inf
            max_bridge = -inf
        else:
            max_including_root_left, max_excluding_root_left, max_bridge_left = maxPathSum(node.left)
            max_including_root_right, max_excluding_root_right, max_bridge_right = maxPathSum(node.right)

            max_including_root = max(max_including_root_left, max_including_root_right) + node.val
            max_excluding_root = max(max_excluding_root_left, max_excluding_root_right,
                                    max_including_root_left + max_including_root_right)
            max_bridge = max(max_bridge_left, max_bridge_right) + node.val

        return max_including_root, max_excluding_root, max_bridge
'''

import numpy as np

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # find the maximum path with the root and one of the subtrees, and the
        # maximum path without the root and one of the subtrees, and the maximum
        # path with the root and the two subtrees.

        max_include_root, max_not_include_root, max_brigde_root = self.maxPath(root)

        # return the maximum of the three
        return max(max_include_root, max_not_include_root, max_brigde_root)
    
    def maxPath(self, node):
        # if the node is empty, return -inf for all three
        if node is None:
            return - np.inf, - np.inf, -np.inf
        
        # find the three maximum values for the left and right subtrees
        max_include_left, max_not_include_left, max_brigde_left = self.maxPath(node.left)
        max_include_right, max_not_include_right, max_brigde_right = self.maxPath(node.right)
        
        # find the maximum path with the root and one of the subtrees
        max_include_node = max(node.val, node.val + max_include_left, 
                               node.val + max_include_right)
        
        # find the maximum path without the root and one of the subtrees
        max_brigde = max(node.val + max_include_left + max_include_right,
                        max_brigde_left, max_brigde_right)
        
        # find the maximum path with the root and the two subtrees
        max_not_include_node = max(max_not_include_left, max_not_include_right,
                                  max_include_left, max_include_right)

        return max_include_node, max_not_include_node, max_brigde
        