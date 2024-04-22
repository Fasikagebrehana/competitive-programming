class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def variations(lock):
            res = []
            for i in range(4):
                s = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + s + lock[i+1:])
                s = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + s + lock[i+1:])
            return res

        visited = set(deadends)
        queue = deque()
        queue.append(("0000", 0))
        while queue:
            lock, turn = queue.popleft()
            if lock == target:
                return turn
            for var in variations(lock):
                if var not in visited:
                    visited.add(var)
                    queue.append((var, turn + 1))
        return -1
        