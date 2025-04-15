class Solution:
    def isPalindrome(self, s: str) -> bool:
        curr = []
        for st in s:
            if st.isalnum():
                curr.append(st.lower())
        return curr[:] == curr[::-1]