'''
A trie (pronounced as "try") or prefix tree is a tree data structure 
used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as 
autocomplete and spellchecker.

Implement the Trie class:

    - Trie() Initializes the trie object.
    - void insert(String word) Inserts the string word into the trie.
    - boolean search(String word) Returns true if the string word is 
    in the trie (i.e., was inserted before), and false otherwise.
    - boolean startsWith(String prefix) Returns true if there is a 
    previously inserted string word that has the prefix prefix, and 
    false otherwise.
'''
class TreeNode:
        def __init__(self):
            self.alphabet = [None] * 26
            self.endOfWord = False
            
        def setEndOfWord(self):
            self.endOfWord = True

        def __str__(self):
            return str(self.alphabet)
class Trie(object):
            
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for c in range(len(word)):
            order = ord(word[c]) - ord('a')
            if current.alphabet[order] is None:
                current.alphabet[order] = TreeNode()
            current = current.alphabet[order]
            if c == len(word) - 1:
                current.setEndOfWord()

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for c in range(len(word)):
            order = ord(word[c]) - ord('a')
            if current.alphabet[order] is None:
                return False
            else:
                current = current.alphabet[order]
            if c == len(word) - 1:
                return current.endOfWord
        
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for c in range(len(prefix)):
            order = ord(prefix[c]) - ord('a')
            if current.alphabet[order] is None:
                return False
            else:
                current = current.alphabet[order]
        return True
        

# Your Trie object will be instantiated and called as such:
word = "apple"
prefix = "app"
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
print(param_2, param_3)