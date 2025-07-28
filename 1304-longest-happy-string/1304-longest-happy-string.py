class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a >0:
            heappush(heap, (-a, 'a'))
        if b > 0:
            heappush(heap, (-b, 'b'))
        if c >0:
            heappush(heap, (-c, 'c'))

        happy = []
        while heap:
            count, ch = heappop(heap)
            if len(happy) >= 2 and happy[-1] == ch and happy[-2] == ch:
                if heap:
                    count2, ch2 = heappop(heap)
                    happy.append(ch2)
                    count2 += 1
                    if count2 < 0:
                        heappush(heap, (count2, ch2))
                    # even if count2 is 0 or greater since we already appended ch2 we can push  ch and count to the heap
                    heappush(heap, (count, ch))
            else:
                happy.append(ch)
                count += 1
                if count < 0:
                    # if the count is still not zero we append it to heap and again we append it to the heap and on the next pop it will pop the max so it can be ch or other
                    heappush(heap, (count, ch))
            
        # print(happy)

        return ''.join(happy)