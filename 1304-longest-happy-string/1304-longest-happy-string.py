class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        
        heap = []
        if a > 0:
            heappush(heap, (-a, 'a'))
        if b > 0:
            heappush(heap, (-b, 'b'))
        if c > 0:
            heappush(heap, (-c, 'c'))

        while heap:
            count, ch = heappop(heap)
            if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch:
                if heap:
                    count2, ch2 = heappop(heap)
                    ans.append(ch2)
                    count2 += 1
                    if count2 < 0:
                        heappush(heap, (count2, ch2))
                    heappush(heap, (count, ch))
            else:
                ans.append(ch)
                count += 1
                if count < 0:
                    heappush(heap, (count, ch))
        return ''.join(ans)

