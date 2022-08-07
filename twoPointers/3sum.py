'''
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, 
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate 
triplets.
'''
class MySolution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # since the triples must be unique, we want to sort the array
        nums = sorted(nums)
        
        # save the result in a list
        result = set()
        
        hashSet = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if -(nums[i] + nums[j]) in hashSet:
                    result.add(tuple([-(nums[i] + nums[j]), nums[i], nums[j]]))
            hashSet.add(nums[i])
            
        return [list(x) for x in list(result)]


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort the list to avoid duplication
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            n = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                # if this number has been seen before, move on
                continue
            # use two pointers start at the beginning and the end of the list
            l, r = i + 1, len(nums) - 1
            #slowly move the pointer towards each other until they meet
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum < 0:
                    # if the sum is less than 0, we want to increase it
                    # since the list is sorted, we can just move the left
                    # pointer towards
                    l += 1
                elif threeSum > 0:
                    # move the right pointer backwards to decrease the sum
                    r -= 1
                else:
                    # if the sum is 0, add the three numbers to the result
                    # list, and move the left pointer forward
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return res