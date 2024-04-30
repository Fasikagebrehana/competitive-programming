class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adjList = defaultdict(list)
        indegree = [0] * len(recipes)

        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                adjList[ingredients[i][j]].append(i)
                indegree[i] += 1

        ans = []
        queue = deque()
        visited = set()
        for i in supplies:
            queue.append(i)
            visited.add(i)
        while queue:
            node = queue.popleft()
            for neighbour in adjList[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    ans.append(recipes[neighbour])
                    print(recipes[neighbour])
                    queue.append(recipes[neighbour])
        # print(indegree)
        return ans