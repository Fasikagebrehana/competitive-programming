class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # create the connection between the equations then create our adjacency relation 

        graph = defaultdict(list)
        for i in range(len(equations)):
            x, y = equations[i]
            graph[x].append((y, values[i]))
            graph[y].append((x, 1 / values[i]))

        # now we need to use a data structure that will traverse through the graph then try to find the target for each queries
        visited = set()

        def dfs(num, target, result):
            if num == target:
                return result
            
            for neigh, weigh in graph[num]:
                if neigh not in visited:
                    visited.add(neigh)
                    # we need to store it to a temporary variable and return, so that it can be returned to the previous caller 
                    temp = dfs(neigh, target, result * weigh)
                    if temp:
                        return temp
            

        answer = []
        for x, y in queries:
            ans = 1
            if x not in graph or y not in graph:
                answer.append(-1)
            elif x == y:
                answer.append(1.0)
            else:
                visited = set()
                visited.add(x)
                ans = dfs(x, y, ans)
                answer.append(ans) if ans else answer.append(-1)
        # print(answer)
        return answer