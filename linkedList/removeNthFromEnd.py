'''
Given the head of a linked list, remove the nth 
node from the end of the list and return its 
head.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        s, t = head, head
        tprev = None
        
        for i in range(n):
            s = s.next
            
        while (s is not None):
            s = s.next
            tprev = t
            t = t.next
        if tprev is None:
            return t.next
        tprev.next = t.next
        return head