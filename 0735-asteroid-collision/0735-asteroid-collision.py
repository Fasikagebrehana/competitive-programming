class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        stack.append(asteroids[0])
        i = 1
        while i < len(asteroids):
            if stack and asteroids[i] < 0 and stack[-1] > 0:
                if abs(asteroids[i]) > stack[-1]:
                    stack.pop()
                elif abs(asteroids[i]) == stack[-1]:
                    stack.pop()
                    i += 1
                else:
                    i += 1
            else:
                stack.append(asteroids[i])
                i += 1
        return stack