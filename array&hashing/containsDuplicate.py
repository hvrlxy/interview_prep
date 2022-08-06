# My Solution: Creating a dictionary (which is implemented as a hash map in Python)
# go through the array and check if the element is in the dictionary, if it is, return True, 
# otherwise, add the element to the dictionary and continue
# Time Complexity: O(n)
# Space Complexity: O(n)
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    numSet = {}
    for n in nums:
        if n not in numSet:
            numSet[n] = 1
        else:
            return True
    return False


# Other's Solution: Using a hashset instead of a dictionary
# Time Complexity: O(n)
# Space Complexity: O(n)
def containsDuplicate(self, nums: list[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False