class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = defaultdict(list)
        for x,y in zip(s1, s2):
            graph[x].append(y)
            graph[y].append(x)
        # print(graph)

        def bfs(l):
            queue = deque([l])
            visited = set()
            min_char = l
            while queue:
                node = queue.popleft()
                visited.add(node)

                for neigh in graph[node]:
                    if neigh not in visited:
                        min_char = min(min_char, neigh)
                        queue.append(neigh)

            return min_char

        store = defaultdict(str)
        answer = []
        visiteds = set()
        for s in baseStr:
            if s not in visiteds:
                minChar = bfs(s)
                answer.append(minChar)
                store[s] = minChar
                visiteds.add(s)
            else:
                answer.append(store[s])
            
            
        # print(answer)

        return ''.join(answer)