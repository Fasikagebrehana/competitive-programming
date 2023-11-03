class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        i = 1
        while i <= target[-1]:
            stack.append("Push")
            if i in target:
                i += 1
            else:
                stack.append("Pop")
                i += 1
        return stack