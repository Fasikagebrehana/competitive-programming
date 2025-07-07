class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        if len(s) == 1:
            return s

        for key, val in counter.items():
            heappush(heap, (-val, key))
        
        # print(heap)
        answer = []

        while heap:
            freq, char = heappop(heap)
            answer.append(char)

            if heap:
                freq2, char2 = heappop(heap)
                answer.append(char2)

                freq2 += 1
                if freq2 < 0:
                    heappush(heap, (freq2, char2))

            freq += 1
            if freq < 0:
                heappush(heap, (freq, char))
            

        # print(answer)
        if answer[-1] == answer[-2]:
            return ""
        else:
            return ''.join(answer)