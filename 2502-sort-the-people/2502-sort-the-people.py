class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        store = {}
        for i in range(len(names)):
            store[heights[i]] = names[i]
        # print(arr)

        for i in range(1, len(names)):
            temp = heights[i]
            j = i - 1
            while j >= 0 and heights[j] < temp:
                heights[j+1] = heights[j]
                j = j- 1
            heights[j+1] = temp
        for i in range(len(heights)):
            names[i] = store[heights[i]]
        return names