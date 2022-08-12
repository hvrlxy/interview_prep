'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along 
the longest path from the root node down to the farthest 
leaf node.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # if the root is empty, depth is 0
        if root is None:
            return 0
        
        # get the depth of the left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # return the greater of the two depths + 1
        return max(left_depth, right_depth) + 1
        