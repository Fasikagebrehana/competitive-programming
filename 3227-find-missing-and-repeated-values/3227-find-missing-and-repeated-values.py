class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        store = defaultdict(int)
        arr = []
        answer = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                arr.append(grid[i][j])
                store[grid[i][j]] += 1
                if store[grid[i][j]] > 1:
                    answer.append(grid[i][j])
        # print(arr)
        # print(answer)
        for i in range(1, (n**2) + 1):
            if i not in store:
                # print(i)   
                answer.append(i)

        return answer
