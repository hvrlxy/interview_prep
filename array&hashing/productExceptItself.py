'''
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums 
except nums[i].

The product of any prefix or suffix of nums is guaranteed to 
fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and 
without using the division operation.
'''
# My Solution:
def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # traverse the list from first to last elements, calculate the prefix product of element
    prefixProduct = [0] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            prefixProduct[i] = 1
        else:
            prefixProduct[i] = prefixProduct[i - 1] * nums[i - 1]
    # traverse the list from last to first element, calculate the suffix product of the current element
    suffixProduct = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            suffixProduct[i] = 1
        else:
            suffixProduct[i] = suffixProduct[i + 1] * nums[i + 1]
    #calculate the product of the array except the given element
    output = []
    for i in range(len(nums)):
        output.append(prefixProduct[i] * suffixProduct[i])
    return output

# Solution: doesn't have to store the prefix and suffix, only have to traverse the list twice
def productExceptSelf(self, nums: list[int]) -> list[int]:
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res