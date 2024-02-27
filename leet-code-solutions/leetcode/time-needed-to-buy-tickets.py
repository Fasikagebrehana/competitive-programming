class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque((i, val) for i, val in enumerate(tickets))
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1
            if curr[1] > 1:
                queue.append((curr[0], (curr[1]-1)))
            if curr[0] == k and curr[1] == 1:
                return count
            
        