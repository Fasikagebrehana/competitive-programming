class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruit = 0
        left = 0
        count = Counter()
        for right in range(len(fruits)):
            count[fruits[right]] += 1
            if len(count) > 2:
                while left < len(fruits) and len(count) > 2:
                    if count[fruits[left]] <= 1:
                        del count[fruits[left]]
                    else:
                        count[fruits[left]] -= 1
                    left += 1
            max_fruit = max(max_fruit, (right - left + 1))
        return max_fruit
                