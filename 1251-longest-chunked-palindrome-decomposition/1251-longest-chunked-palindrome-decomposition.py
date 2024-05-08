class Solution:
    def longestDecomposition(self, text: str) -> int:
        left = []
        right = []
        l, r = 0, len(text) - 1
        count = 0
        while l <= r:
            left.append(text[l])
            right.append(text[r])
            if left == right[::-1] and l < r:
                count += 2
                left = []
                right = []
            l += 1
            r -= 1

        if left and right:
            count += 1
        return count
            