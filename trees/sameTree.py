'''
Given the roots of two binary trees p and q, 
write a function to check if they are the 
same or not.

Two binary trees are considered the same if 
they are structurally identical, and the nodes 
have the same value.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # if both trees are empty, return True
        if p is None and q is None:
            return True
        # if one of the trees is empty, return False
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        # if the values of the trees are not equal, return False
        if p.val != q.val:
            return False
        
        # check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        