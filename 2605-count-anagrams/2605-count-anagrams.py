class Solution:
    def countAnagrams(self, s: str) -> int:
        words = s.split(' ')
        answer = 1
        # print(len(s))
        # counter length = 4

        for word in words:
            counter = Counter(word)
            n = math.factorial(len(word))
            d = 1
            for val in counter.values():
                d *= math.factorial(val)

            permutation = n // d
            answer *= permutation
        # print(answer)

        return answer % (10**9 + 7)