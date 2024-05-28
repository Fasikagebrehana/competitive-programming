class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = set()
        for s in sentence:
            letters.add(s)

        return True if len(letters) == 26 else False