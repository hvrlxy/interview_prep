'''
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every 
character in t (including duplicates) is included in the 
window. If there is no such substring, return the empty 
string "".

The testcases will be generated such that the answer is 
unique.

A substring is a contiguous sequence of characters within 
the string.
'''

class MySolution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        # put all letters into a dictionary for O(1) lookup
        letters = {c:t.count(c) for c in t}
        
        # initialize the left pointer
        l = 0
        
        # save the shortest length of the substring in a variable
        shortest = 10**5
        shortest_indices = (0, 0)
        
        for r in range(len(s)):
            if s[r] not in letters:
                continue
            letters[s[r]] -= 1
            if sorted(list(letters.values()), reverse = True)[0] > 0:
                continue
            while s[l] not in letters or letters[s[l]] < 0:
                if s[l] in letters: letters[s[l]] += 1
                l += 1
            length = r - l + 1
            if length < shortest:
                shortest = length
                shortest_indices = (l, r)
        if shortest == 10**5:
            return ""
        return s[shortest_indices[0]:shortest_indices[1]+1]

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                # pop from the left of our window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""