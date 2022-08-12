'''
Given the roots of two binary trees root and subRoot, 
return true if there is a subtree of root with the 
same structure and node values of subRoot and false 
otherwise.

A subtree of a binary tree tree is a tree that consists 
of a node in tree and all of this node's descendants. The 
tree tree could also be considered as a subtree of itself.
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
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
    
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        