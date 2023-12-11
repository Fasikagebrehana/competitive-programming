class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic1 = {}
        dic2 = {}
        result = []
        m = max(len(list1), len(list2))
        index_sum = 0
        for i in range(len(list1)):
            dic1[list1[i]] = i
        for j in range(len(list2)):
            dic2[list2[j]] = j
        
        min_index_sum = float('inf')
        for st in dic1:
            if st in dic2:
                curr_sum = dic1[st] + dic2[st]
                if curr_sum < min_index_sum:
                    result = [st]
                    min_index_sum = curr_sum
                elif curr_sum == min_index_sum:
                    result.append(st)

        return result