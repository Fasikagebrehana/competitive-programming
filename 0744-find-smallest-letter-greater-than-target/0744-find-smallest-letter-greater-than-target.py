class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for ch in letters:
            if target < ch:
                return ch
        return letters[0]