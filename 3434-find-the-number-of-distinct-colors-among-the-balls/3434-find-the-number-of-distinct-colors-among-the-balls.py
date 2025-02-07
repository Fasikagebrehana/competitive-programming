class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color = defaultdict(int)
        ball = defaultdict(list)
        answer = []
        for x, y in queries:
            if x in ball:
                color[ball[x]] -= 1
                if color[ball[x]] == 0:
                    del color[ball[x]]
            ball[x] = y
            color[y] += 1
            answer.append(len(color))
            
        # print(color)
        # print(ball)
        # print(answer)

        return answer