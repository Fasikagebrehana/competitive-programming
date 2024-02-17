class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # temp = ""
        # for i in range(len(s)//2):
        #     temp = s[i]
        #     s[i] = s[len(s)-1-i]
        #     s[len(s)-i-1] = temp
        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1