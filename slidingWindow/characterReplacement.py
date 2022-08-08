'''
You are given a string s and an integer k. 
You can choose any character of the string 
and change it to any other uppercase English 
character. You can perform this operation at 
most k times.

Return the length of the longest substring 
ontaining the same letter you can get after 
performing the above operations.


'''
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        #set a slow pointer at the beginning of the string
        l = 0
        longest = 0
        freq = {} #store the character frequency
        
        # store the maxFrequency character of a substring
        maxf = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            # to update the maxf variable, we only need to compare the maxf variable
            # to the current character's frequency
            maxf = max(maxf, freq[s[r]])
            
            # calculate current length of the substring
            current_length = r - l + 1
            if current_length - maxf > k:
                # if the current length of the string subtracting the maxfreq 
                # chracter exceed k, we know that we have performed more than
                # k operations. We increment the counter and pop the leftward 
                # character off the dictionary
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
            
        return longest