'''
Suppose an array of length n sorted in ascending 
order is rotated between 1 and n times. For 
example, the array nums = [0,1,2,4,5,6,7] might 
become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], 
a[2], ..., a[n-1]] 1 time results in the array 
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique 
elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) 
time.
'''
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if mid == 0 and nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif mid == len(nums) - 1 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif mid != 0 and mid != len(nums) - 1 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            #check for which part is sorted
            if nums[l] <= nums[mid]:
                # [2, 3, 4, 5, 6, 0, 1]
                if nums[mid] > nums[r]:
                    l = mid + 1
                # [0, 1, 2, 3, 4, 5, 6]
                else:
                    r = mid - 1
            else:
                # [5, 6, 0, 1, 2, 3, 4]
                # [5,1,2,3,4]
                if nums[mid] < nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1