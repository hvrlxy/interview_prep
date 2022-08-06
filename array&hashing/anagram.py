# My Solution: store letters of both string into dictionaries and compare the two dictionaries
# Time Complexity: O(n)
# Space Complexity: O(n)
def isAnagram(self, s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # check if they have the same length
    if len(s) != len(t):
        return False
    
    # create a dictionary to store the occurences of the letters in both words
    s_count = {}
    t_count = {}
    
    for i in range (len(s)):
        # check if the letter exists in the dictionary, if not, add to the dict
        if s[i] not in s_count:
            s_count[s[i]] = 1
        else:
            s_count[s[i]] += 1
        if t[i] not in t_count:
            t_count[t[i]] = 1
        else:
            t_count[t[i]] += 1
    
    # check if the two dictinaries are similar
    return s_count == t_count

# Solution: write code more efficiently than I did, with type annotations
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT