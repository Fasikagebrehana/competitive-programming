class Solution:
    def splitString(self, s: str) -> bool:
        arr = []
        def helper(index):
            # base case
            if index >= len(s):
                for idx in range(1, len(arr)):
                    if arr[idx-1]- arr[idx] != 1:
                        return False
                return len(arr) >= 2

            
            for i in range(index, len(s)):
                val = int(s[index:i+1])
                if not arr or arr[len(arr)-1] - val == 1:
                    arr.append(val)
                    if helper(i+1):
                        return True
                    arr.pop()
                
            return False

        return helper(0)