class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        for x, y in adjacentPairs:
            adjList[x].append(y)
            adjList[y].append(x)
        
        answer = []
        queue = deque()
        visited = set()
        for key, val in adjList.items():
            if len(val) == 1:
                queue.append(key)
                visited.add(key)
                break
        
        while queue:
            node = queue.popleft()
            answer.append(node)
            for neigh in adjList[node]:
                if neigh not in visited:
                    queue.append(neigh)
                    visited.add(neigh)
        # print(answer)
        return answer