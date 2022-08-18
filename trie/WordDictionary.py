class TreeNode:
        def __init__(self):
            self.alphabet = [None] * 26
            self.endOfWord = False
            
        def setEndOfWord(self):
            self.endOfWord = True

        def __str__(self):
            return str(self.alphabet)
        
class WordDictionary(object):

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word):
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
        return self.searchSuffix(word, self.root)
    
    def searchSuffix(self, suffix, node):
        c = suffix[0]
        if c == suffix and c == '.':
            for i in range(26):
                if node.alphabet[i] is not None:
                    return node.alphabet[i].endOfWord
            return False
        elif c == suffix:
            order = ord(c) - ord('a')
            return node.alphabet[order].endOfWord
        elif c == '.':
            found = False
            for i in range(26):
                if node.alphabet[i] is not None:
                    found = found or self.searchSuffix(suffix[1:], node.alphabet[i])
            return found
        else:
            order = ord(c) - ord('a')
            if node.alphabet[order] is not None:
                return self.searchSuffix(suffix[1:], node.alphabet[order])
            else:
                return False
                
        return False
        
# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
words = ['bad', 'dad', 'mad', 'rad', 'dad']
for word in words:
    obj.addWord(word)
searches = ['pad', 'b..', 'd..']
for word in searches:
    print(word, obj.search(word))
    print('\n')