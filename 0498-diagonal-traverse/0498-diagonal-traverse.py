class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        ans = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                key = i + j
                dic[key].append(mat[i][j])
        for key in dic:
            if key % 2 == 0:
                ans.extend(dic[key][::-1])
            else:
                ans.extend(dic[key])
        return ans