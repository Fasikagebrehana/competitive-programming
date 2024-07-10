class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for l in logs:
            if l == "../" and stack:
                stack.pop()
            elif l == "../" and not stack:
                continue
            elif l == "./":
                continue
            else:
                stack .append(l)
        return len(stack)