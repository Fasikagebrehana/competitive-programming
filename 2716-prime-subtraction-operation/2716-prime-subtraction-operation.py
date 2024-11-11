class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = []
        n = 1000
        is_prime = [True for _ in range(n + 1)]
        is_prime[0] = is_prime[1] = False
        d = 2
        while d <= n:
            if is_prime[d]:
                j = 2 * d
                while j <= n:
                    is_prime[j] = False
                    j += d
            d += 1
        for i in range(len(is_prime)):
            if is_prime[i]:
                primes.append(i)
        # print(len(primes))
        prev = 0
        for i in range(len(nums)):
            if nums[i] <= prev:
                return False
            idx = bisect_left(primes, nums[i] - prev) - 1
            if idx != -1:
                nums[i] -= primes[idx]
            prev = nums[i]
        return True