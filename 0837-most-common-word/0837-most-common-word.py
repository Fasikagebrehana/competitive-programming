class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = re.split(r'\W+', paragraph)
        counter = defaultdict(int)
        for i in p:
            temp = i.lower()
            counter[temp] += 1
        print(counter)
        max_freq = ""
        freq = 0
        for key, val in counter.items():
            if key not in banned and freq < val and key.isalpha():
                max_freq = key
                freq = val
        return max_freq           