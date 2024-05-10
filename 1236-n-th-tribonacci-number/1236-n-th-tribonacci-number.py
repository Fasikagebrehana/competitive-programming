class Solution:
    def tribonacci(self, n: int) -> int:
        store = {}
        def fib(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n not in store:
                store[n] = fib(n-1) + fib(n-2) + fib(n-3)
            return store[n]
        return fib(n)