'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and 
(i, height[i]).

Find two lines that together with the x-axis form 
a container, such that the container contains the 
most water.

Return the maximum amount of water a container can 
store.

Notice that you may not slant the container.


'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # save the current max area of water possible
        max_area = 0
        
        # initialize 2 pointers
        l, r = 0, len(height) - 1
        # slowly move the two pointers towards each other until they meet
        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > max_area:
                max_area = area
            
            # check for the shorter stick
            if height[l] < height[r]:
                # if left is the shorter stick, move the pointer forward
                # until we find a longer one, or meet the right stick
                current_height = height[l]
                l += 1
                while height[l] < current_height:
                    l += 1
            else:
                # if right is the shorter stick, move the pointer backward
                # until we find a longer one, or meet the left stick
                current_height = height[r]
                r -= 1
                while height[r] < current_height:
                    r -= 1
        return max_area
        
        