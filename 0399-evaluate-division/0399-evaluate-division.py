class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
        
        # print(graph)
        
        visited = set()
        def dfs(curr, target, ans):
            nonlocal result
            if curr == target:
                result = ans
                return
            visited.add(curr)
            
            for neigh, weigh in graph[curr]:
                if neigh not in visited:
                    dfs(neigh, target, ans * weigh)
        evaluation = [] 
        for x, y in queries:
            result = None
            ans = 1
            if x not in graph or y not in graph:
                evaluation.append(-1.0)
                continue
            elif x == y:
                evaluation.append(1.0)
                continue
            else:
                visited = set()
                if x not in visited:
                    visited.add(x,)
                    dfs(x, y, ans)
                   
            if result is not None:
                evaluation.append(result)
            else:
                evaluation.append(-1)
        return evaluation