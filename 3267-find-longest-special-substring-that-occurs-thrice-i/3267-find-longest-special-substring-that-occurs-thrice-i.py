class Solution:
    def maximumLength(self, s: str) -> int:
        left = 0
        substring = -1
        store = defaultdict(int)
        left = 0
        for i in range(len(s)):
            if s[i] != s[left]:
                size = (i - left)
                maxx = size
                j = size
                #  and maxx >= 3
                while j > 0:
                    store[(s[left], j)] += size - j + 1
                    # maxx = 
                    j -= 1
                left = i
            

            # elif left == i and i == len(s) - 1:
            #     print(s[i])
        size = (i - left + 1)
        maxx = size
        j = size
        #  and maxx >= 3
        while j > 0:
            store[(s[left], j)] += size - j + 1
            # maxx = 
            j -= 1
            #     left = i

        # print(store)
        
        max_substring = -1
        for key, val in store.items():
            if val >= 3:
                max_substring = max(max_substring, key[1])
        return max_substring