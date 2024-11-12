class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        # queries.sort()
        maxx = items[0][1]
        firstElements = []
        for i in range(len(items)):
            if items[i][1] < maxx:
                items[i][1] = maxx
            else:
                maxx = max(maxx, items[i][1])
            firstElements.append(items[i][0])
        # print(items)
        if len(items) == 1:
            if queries[0] < items[0][0]:
                return [0]
        answer = []
        for num in queries:
            idx = bisect_right(firstElements, num)
            if idx == 0:
                answer.append(0)
            else:
                answer.append(items[idx-1][1])
        # print(answer)
        return answer