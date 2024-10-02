class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        ans = []
        
        dic = {}
        flag = False
        count = 0
        for i in range(len(sorted_arr)):
            if sorted_arr[i] not in dic and flag == False:
                dic[sorted_arr[i]] = i + 1
            elif flag and sorted_arr[i] not in dic:
                dic[sorted_arr[i]] = i + 1 - count
            else:
                flag = True
                count += 1
        
        for num in arr:
            ans.append(dic[num])
        return ans