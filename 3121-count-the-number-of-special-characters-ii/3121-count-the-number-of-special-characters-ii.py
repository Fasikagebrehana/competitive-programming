class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # keep track of the index of each appearance of characters
        lowers = defaultdict(list)
        uppers = defaultdict(list)
        # print(ord('z'))

        for i in range(len(word) - 1, -1, -1):
            if 97 <= ord(word[i]) < 123:
                lowers[word[i]].append(i)
            else:
                uppers[word[i]].append(i)

        # print(lowers)
        # print(uppers)
        special = 0
        for ch, idx in lowers.items():
            if ch.upper() in uppers and max(idx) < min(uppers[ch.upper()]):
                special += 1
        return special
