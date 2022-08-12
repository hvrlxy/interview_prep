'''
Given a binary search tree (BST), find the lowest common ancestor 
(LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest 
common ancestor is defined between two nodes p and q as the lowest 
node in T that has both p and q as descendants (where we allow a 
node to be a descendant of itself).”
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #check if the root is empty
        if not root:
            return [False, False]
        
        # if root is not a leaf, call recursion of the left and right child
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if isinstance(left, TreeNode):
            return left
        if isinstance(right, TreeNode):
            return right
        
        result = [left[0] or right[0], left[1] or right[1]]
        print(root.val, result)
        if result[0] and result[1]:
            return root

        if root.val == p.val:
            result[0] = True
        if root.val == q.val:
            result[1] = True
        if result[0] and result[1]:
            return root
        return result
        
        
        