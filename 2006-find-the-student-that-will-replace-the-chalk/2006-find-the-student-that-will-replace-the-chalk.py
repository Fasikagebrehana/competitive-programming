class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # ans = 0
        # summ = 0
        # def check():
        #     nonlocal summ
        #     for i in range(len(chalk)):
        #         summ += chalk[i]
        #         if summ >= k:
        #             return i
        #     return


        # left, right = 0, len(chalk) - 1
        # while left <= right:
        #     middle = (right - left) // 2
        #     if check(middle):

        prefix = [0] * len(chalk)
        prefix[0] = chalk[0]
        for i in range(1, len(chalk)):
            prefix[i] += chalk[i] + prefix[i-1]
        if len(chalk) == 1:
            return 0
        while k > 0:
            idx = bisect_left(prefix, k)
            if idx >= len(chalk):
                k -= prefix[-1]
            else:
                if k == prefix[idx]:
                    return (idx + 1) % len(chalk)
                else:
                    return idx