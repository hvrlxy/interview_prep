'''
Given an unsorted array of integers nums, return the 
length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''


'''
Solution:
Put all the number into a set for O(1) lookup

Loop through all the numbers in the set.
Take a number n and check if n-1 is in the set.
If it is, then we know that n is not the start of 
the longest consecutive sequence.
If n-1 is not in the set, then we know that n might
be the start of a consecutive sequence. We keep checking
if n+1, n+2, ... are in the set until we have built the
longest consecutive sequence starting with n.
'''
def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if its the start of a sequence
        if (n - 1) not in numSet:
            length = 1
            while (n + length) in numSet:
                length += 1
            longest = max(length, longest)
    return longest