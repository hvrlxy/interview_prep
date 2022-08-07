'''
Given an integer array nums and an integer k,
return the k most frequent elements. You may 
return the answer in any order.
'''
def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # create the dictionary that store the occurences of the numbers
    occurences = {}
    
    for n in nums:
        occurences[n] = 1 + occurences.get(n, 0)
    
    occurences_items = sorted(list(occurences.items()), key = lambda x: x[1], reverse = True)
    result = [x[0] for x in occurences_items]
    return result[0:k]

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res
