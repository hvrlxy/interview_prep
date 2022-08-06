'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using all 
the original letters exactly once.
'''

def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # creating a dictionary to store the different groups of anagram
    hashSet = {}
    
    # We can create a hash tuples for each of the string. 
    # If they have similar hash tuples, they are 
    # anagrams.
    for astr in strs:
        hashTuples = [0] * 26
        for c in astr:
            hashTuples[ord(c) - ord('a')] += 1
        hashTuples = tuple(hashTuples)
        if hashTuples not in hashSet:
            hashSet[hashTuples] = [astr]
        else:
            hashSet[hashTuples] += [astr]
            
    return hashSet.values()