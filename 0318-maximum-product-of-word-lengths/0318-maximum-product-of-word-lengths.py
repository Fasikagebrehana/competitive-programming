class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        def helper(word):
            bit = 0
            for ch in word:
                bit |= 1 << (ord(ch) - ord('a'))
            return bit

        arr = []
        for word in words:
            temp = helper(word)
            arr.append(temp)
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not arr[i] & arr[j]:
                    ans = max(ans, len(words[i]) * len(words[j]))
        
        return ans