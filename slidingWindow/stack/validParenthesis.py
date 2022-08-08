'''
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if 
the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type 
of brackets.
Open brackets must be closed in the correct 
order.
'''

from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = deque()
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            else:
                if len(stack) == 0 or stack.pop() != '[':
                    return False
        return len(stack) == 0