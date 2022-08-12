'''
You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted 
linked-list and return it.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        new_list = []
        for alist in lists:
            if alist is not None:
                new_list.append(alist)
        lists = new_list
        
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        
        heapq.heapify(lists)
        head = ListNode(0, None)
        current = head
        while (len(lists) > 0):
            smallest_head = heapq.heappop(lists)
            next_list = smallest_head.next
            smallest_head.next = None
            if next_list is not None:
                heapq.heappush(lists, next_list)
            current.next = smallest_head
            current = current.next
        
        return head.next