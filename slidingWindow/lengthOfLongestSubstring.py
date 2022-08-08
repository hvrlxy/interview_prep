class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        
        charSet = set()
        
        # initialize two pointers, pointing to the first and last character of a substring
        l, r = 0, 0
        
        #store the length of the longest substring so far, we will start at the first character 
        # of the string
        longest = 1
        charSet.add(s[0])
        while r < len(s) - 1:
            # increase the right pointer until we find a character that is in the set
            while r < len(s) - 1 and s[r + 1] not in charSet:
                # for each new character, add it to the set and increment the right pointer
                r += 1
                charSet.add(s[r])
            # update the longest substring if the current substring is longer than the previous longest
            longest = max(longest, len(charSet))
            
            # if we reach the end of the string, we are done
            if r == len(s) - 1:
                break
            
            nextChar = s[r + 1]
            # increment the left pointer until we find nextChar
            while(s[l] != nextChar):
                charSet.remove(s[l])
                l += 1
            # increment the left pointer
            charSet.remove(s[l])
            l += 1
                
        return longest