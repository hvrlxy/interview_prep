'''
You are given the heads of two sorted linked lists 
list1 and list2.

Merge the two lists in a one sorted list. The list 
should be made by splicing together the nodes of 
the first two lists.

Return the head of the merged linked list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        curr = ListNode(0, None)
        head1 = list1
        head2 = list2
        
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                curr.next = head1
                curr = curr.next
                head1 = head1.next
            else:
                curr.next = head2
                curr = curr.next
                head2 = head2.next
        
        if head1 is None:
            curr.next = head2
        if head2 is None:
            curr.next = head1
            
        if list1.val <= list2.val:
            return list1
        else:
            return list2