# My Solution: use a hashset to store the indices of the elements in the array as
# we go through the array. If we find an reciprocate element in the hashset, return True.
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    # create a set to store the passing numbers
    hashSet = {}
    # loop through the list, for each number n, check to see if target - n
    # already exists. If yes, return the indices of n and target - n, else, keep
    # looping
    for i in range(len(nums)):
        if (target - nums[i]) in hashSet:
            return [i, hashSet[target - nums[i]]]
        else:
            hashSet[nums[i]] = i
    # return an invalid answer if there are no pairs found
    return [-1, -1]