class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = []
        for i in range(1, n+1):
            queue.append(i)
        count = 0
        i = 0
        while len(queue) > 1:
            i = (i + k - 1) % len(queue)
            queue.pop(i)
        return queue[0]