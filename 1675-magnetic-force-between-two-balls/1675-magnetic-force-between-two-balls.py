class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def helper(middle):
            count = 1
            prev = position[0]
            for i in range(1, len(position)):
                if position[i] - prev >= middle:
                    count += 1
                    prev = position[i]
                if count == m:
                    return True
            return False

        ans = 0
        low, high = 1, position[len(position)-1] - position[0]
        while low <= high:
            middle = (low + high) // 2
            if helper(middle):
                ans = middle
                low = middle + 1
            else:
                high = middle - 1
        return ans