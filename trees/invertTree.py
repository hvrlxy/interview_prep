'''
Given the root of a binary tree, invert the tree, and return its root.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # if the root is empty, return the root
        if root is None:
            return root
        
        # invert the left and right subtrees
        left_child = root.left
        right_child = root.right
        
        root.right = left_child
        root.left = right_child
        
        # call recursively on the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # return the root
        return root
        
        