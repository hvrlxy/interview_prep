'''
Given two integer arrays preorder and inorder where preorder 
is the preorder traversal of a binary tree and inorder is the 
inorder traversal of the same tree, construct and return the 
binary tree.

Main idea:
1. The preorder list tell us the value of the root node of the tree (the first element in the list).
2. Find the index of the root node in the inorder list.
3. The left subtree is the part of the inorder list before the root node.
4. The right subtree is the part of the inorder list after the root node.

Example:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Visualization:
     3
    / \
   9   20
      /  \
    15    7

preorder = [3,9,20,15,7]
            ^
           root

inorder = [9,3,15,20,7]
        = [9] 3 [15 20 7]
           ^        ^   
    left subtree  right subtree
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.pointer = 0
        
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #set up a pointer to the current root node
        self.pointer = 0

        def recursiveBuild(preorder, inorder):
            # if the inorder list is empty, return None since the tree is empty
            if len(inorder) == 0:
                return None
            
            # the root node is always the first element in the preorder list 
            # (or the one where the pointer is currently at)
            root = TreeNode(preorder[self.pointer], None, None)

            # find the index of the root node in the inorder list
            split_point = -1
            for i in range(len(inorder)):
                if root.val == inorder[i]:
                    split_point = i
                    break

            # the left side of the split point (the root node in the inorder list) 
            # is the left subtree
            left_inorder = inorder[0:split_point]
            # the right side of the split point (the root node in the inorder list)
            # is the right subtree
            right_inorder = inorder[split_point + 1:]
            
            # increment the pointer to the next element in the preorder list
            self.pointer += 1
            # build the left subtree
            root.left = recursiveBuild(preorder, left_inorder)
            # build the right subtree
            root.right = recursiveBuild(preorder, right_inorder)
            
            return root
            
        return recursiveBuild(preorder, inorder)