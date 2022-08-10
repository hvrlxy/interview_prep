'''
You are given the head of a singly linked-list. 
The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. 
Only nodes themselves may be changed.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        # find the middle point of the linked list by using 
        # the fast/slow pointer approach
        mid = None
        s, t = head, head
        while t is not None and t.next is not None:
            mid = s
            s = s.next
            t = t.next.next

        # reverse the second half of the list, with s is the head
        snext = None
        sprev = None
        while s is not None:
            snext = s.next
            s.next = sprev
            
            sprev = s
            s = snext
        
        #start reordering
        t, s = sprev, head
        
        snext = s.next
        tnext = t.next
        while(snext is not None) and (tnext is not None):
            s.next = t
            t.next = snext
            
            s, t = snext, tnext
            snext = snext.next
            tnext = tnext.next
        
        