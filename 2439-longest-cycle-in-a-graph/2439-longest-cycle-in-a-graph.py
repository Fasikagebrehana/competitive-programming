class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        adjList = defaultdict(list)
        for i in range(len(edges)):
            if edges[i] != -1:
                adjList[i].append(edges[i])

        print(adjList)

        def dfs(color, node):
            nonlocal cycle_length
            color[node] = 'grey'
            for neighbour in adjList[node]:
                if color[neighbour] == 'white':
                    parent[neighbour] = node
                    dfs(color, neighbour)
                elif color[neighbour] == 'grey':
                    # cycle
                    curr_length = 1
                    curr = node
                    while curr != neighbour:
                        curr = parent[curr]
                        curr_length += 1
                    cycle_length = max(cycle_length, curr_length)
            color[node] = 'black'
            

        
        parent = [-1] * len(edges)
        color = ['white'] * len(edges)
        cycle_length = 0

        for i in range(len(edges)):
            if color[i] == 'white':
                dfs(color, i)
        return cycle_length if cycle_length != 0 else -1