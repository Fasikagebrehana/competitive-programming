class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        p = [arr[0]]
        for i in range(1, len(arr)):
            p.append(p[i-1] ^ arr[i])
        # print()
        # print(p)
        ans = []
        for left, right in queries:
            if left != 0:
                ans.append(p[left-1] ^ p[right])
            else:
                ans.append(p[right])
            
        return ans