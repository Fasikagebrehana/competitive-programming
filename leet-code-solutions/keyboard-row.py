class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"),
                set("asdfghjkl"),
                set("zxcvbnm")]
        ans = []
        for word in words:
            w = set(word.lower())
            for row in rows:
                if w.issubset(row):
                    ans.append(word)
                    break
                
        return ans