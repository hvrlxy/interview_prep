'''
A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing all 
non-alphanumeric characters, it reads the same forward and 
backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false 
otherwise.
'''
def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    # remove white space and non-alphabet characters from the string
    s = s.lower().replace(' ', '') # lowercase s
    new_s = ''
    for c in s:
        if c.isalpha() or c.isdigit():
            new_s += c
    
    pt1 = 0
    pt2 = len(new_s) - 1
    
    while pt1 < len(new_s)//2:
        if new_s[pt1] != new_s[pt2]:
            return False
        else:
            pt1 += 1
            pt2 -= 1
    return True