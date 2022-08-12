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
        # remove empty lists
        new_list = []
        for alist in lists:
            if alist is not None:
                new_list.append(alist)
        lists = new_list
        
        # add a comparator between the nodes
        setattr(ListNode, "__lt__", lambda self, other: self.val <= other.val)
        
        # sort the lists
        heapq.heapify(lists)
        #initialize the head of the merged list
        head = ListNode(0, None)
        #initilize the pointer to the tail of the merged list
        current = head
        #while there are still lists to be merged
        while (len(lists) > 0):
            smallest_head = heapq.heappop(lists)    #get the smallest nodes
            next_list = smallest_head.next          #get the next node of the smallest node
            smallest_head.next = None               #detach the smallest node from the list
            if next_list is not None:
                heapq.heappush(lists, next_list)    #push the next node of the smallest node to the merge list
            # append the smallest node to the merged list
            current.next = smallest_head
            # move the pointer to the tail of the merged list
            current = current.next
        
        return head.next