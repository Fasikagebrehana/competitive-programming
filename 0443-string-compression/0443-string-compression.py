class Solution:
    def compress(self, chars: List[str]) -> int:
        idx = 0
        start = 0
        while start < len(chars):
            curr = start
            count = 0
            while curr < len(chars) and chars[curr] == chars[start]:
                curr += 1
                count += 1
            chars[idx] = chars[start]
            idx += 1
            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1
            start = curr
        return idx