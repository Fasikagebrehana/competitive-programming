class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = []
        counter = Counter(s)
        # print(counter)
        for key in counter:
            heappush(heap, -(ord(key) - ord('a') + 1))
        # print(heap)
        answer = []
        while heap:
            ch = heappop(heap)
            if counter[chr(-(ch)+ord('a') -1)] <= repeatLimit:
                answer.append(chr(-(ch)+ord('a')-1) * counter[chr(-(ch)+ord('a')-1)])
                counter[chr(-(ch)+ord('a')-1)] -= counter[chr(-(ch)+ord('a')-1)]
            else:
                # print(chr(-(ch)+ord('a')))
                answer.append(chr(-(ch)+ord('a')-1) * repeatLimit)
                counter[chr(-(ch)+ord('a')-1)] -= repeatLimit
                # print(counter[chr(-(ch)+ord('a'))] )
                if counter[chr(-(ch)+ord('a')-1)] > 0 and heap:
                    next = heappop(heap)
                    # print(chr(-(next)+ord('a')))
                    answer.append(chr(-(next)+ord('a')-1))
                    counter[chr(-(next)+ord('a')-1)] -= 1
                    if counter[chr(-(next)+ord('a')-1)] > 0:
                        heappush(heap, next)
                    heappush(heap, ch)
        return (''.join(answer))
