class Solution:
    def findScore(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        heap = []
        for i in range(len(nums)):
            heappush(heap, (nums[i], i))
        # print(heap)
        score = 0
        marked = set()

        while heap and len(marked) <= len(nums):
            element = heappop(heap)
            # print(element)
            if element[1] not in marked:
                score += element[0]
                marked.add(element[1])
                i = element[1]
                if element[1] == 0:
                    marked.add(i+1)
                elif element[1] == len(nums) -1:
                    marked.add(i-1)
                else:
                    marked.add(i+1)
                    marked.add(i-1)
                # print(marked, score)
        return score