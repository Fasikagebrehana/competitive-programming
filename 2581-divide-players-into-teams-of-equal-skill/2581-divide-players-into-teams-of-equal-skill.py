class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        summ = sum(skill)
        team = len(skill) // 2
        if summ % team != 0:
            return -1
        # print(summ % team)
        
        each = summ // team
        # print(each)
        dic = {}
        chemistry = 0
        t = 0
        for s in skill:
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1

        for s in skill:
            if dic[s] > 0:
                if (each - s) in dic and dic[each - s] > 0:
                    chemistry += ((each - s) * s)
                    dic[each - s] -= 1
                    dic[s] -= 1
                # if dic[each - s] == 0:
                #     del dic[each - s]
                else:
                    return -1
           
                
        print(dic)
        print(t)
        return chemistry