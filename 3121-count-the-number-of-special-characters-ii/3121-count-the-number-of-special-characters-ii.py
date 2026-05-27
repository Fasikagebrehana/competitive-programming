class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # keep track of the index of each appearance of characters
        lowers = defaultdict(int)
        uppers = defaultdict(int)
        print(ord('A'))

        for i in range(len(word) - 1, -1, -1):
            if word[i] not in lowers and 97 <= ord(word[i]) < 123:
                lowers[word[i]] = i
            elif ord(word[i]) < 97:
                uppers[word[i]] = i

        # print(lowers)
        # print(uppers)
        special = 0
        for ch, idx in lowers.items():
            if ch.upper() in uppers and idx < uppers[ch.upper()]:
                special += 1
        return special
