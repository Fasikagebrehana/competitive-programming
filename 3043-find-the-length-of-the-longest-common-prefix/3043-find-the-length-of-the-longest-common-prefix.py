class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        longest_prefix = 0
        prefix = set()
        def prefixcalc(n):
            while n > 0:
                rem = n % 10
                n //= 10
                prefix.add((n *10) + rem)
            
        for num in arr1:
            prefixcalc(num)
        
        for num in arr2:
            while num > 0:
                rem = num % 10
                num //= 10
                curr = (num *10) + rem
                if curr in prefix:
                    longest_prefix = max(longest_prefix, len(str(curr)))
        return longest_prefix