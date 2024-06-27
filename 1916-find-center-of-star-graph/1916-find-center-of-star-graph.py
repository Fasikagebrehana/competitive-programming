class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for x, y in edges:
            adjList[x].append(y)
            adjList[y].append(x)
            if len(adjList[x]) > 1:
                return x
            elif len(adjList[y]) > 1:
                return y