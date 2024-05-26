class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class Solution:
    def __init__(self):
        self.trie = TrieNode()
    
    def insert(self, word: str):
        temp = self.trie
        for s in word:
            t = ord(s) - ord('a')
            if temp.children[t] == None:
                temp.children[t] = TrieNode()
            temp = temp.children[t]
        temp.is_end = True

    def find(self, word):
        temp = self.trie
        ans = []
        for s in word:
            t = ord(s) - ord('a')
            if temp.children[t] == None:
                break
            temp = temp.children[t]
            ans.append(s)
            if temp.is_end:
                return ''.join(ans)
        return word            

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        for root in dictionary:
            self.insert(root)
        ans = []
        for word in words:
            ans.append(self.find(word))
        return ' '.join(ans)