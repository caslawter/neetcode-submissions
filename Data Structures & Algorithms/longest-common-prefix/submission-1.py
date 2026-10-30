class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)

        prefix = trie.getCommonPrefix()
        return prefix

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEndOfWord = True

    def getCommonPrefix(self) -> str:
        prefix = ""
        curr = self.root

        while curr.isEndOfWord is not True:
            prefixKey = None
            if curr and len(curr.children) == 1:
                for key in curr.children.keys():
                    prefixKey = key
                    print(key)
                prefix += prefixKey
                curr = curr.children[prefixKey]
            else:
                break
        return prefix