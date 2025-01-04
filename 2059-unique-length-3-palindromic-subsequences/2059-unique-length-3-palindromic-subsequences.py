class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        store = defaultdict(list)
        for i in range(len(s)):
            if s[i] not in store:
                store[s[i]].append(i)
            else:
                store[s[i]].append(i)
        # print(store)
        answer = 0
        for key, val in store.items():
            checker = set()
            if len(val) > 1:
                for i in range(val[0] + 1, val[-1]):
                    checker.add(s[i])
                answer += len(checker)

        # print(answer)
        return answer