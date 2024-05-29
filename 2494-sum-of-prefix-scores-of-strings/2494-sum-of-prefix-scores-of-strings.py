class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
        self.count = 0

    
class Solution:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.trie
        for s in word:
            t = ord(s) - ord('a')
            if temp.children[t] == None:
                temp.children[t] = TrieNode()
            temp = temp.children[t]
            temp.count += 1
        temp.is_end = True

    def search(self, word):
        
        temp = self.trie
        c = 0
        for s in word:
            t = ord(s) - ord('a')
            temp = temp.children[t]
            c += temp.count
        return c
        
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.insert(word)
        ans = []
        for word in words:
            ans.append(self.search(word))
        return ans