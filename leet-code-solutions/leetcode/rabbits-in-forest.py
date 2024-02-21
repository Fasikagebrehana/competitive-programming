class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic = {}
        for ans in answers:
            if ans in dic:
                dic[ans] += 1
            else:
                dic[ans] = 1
        # multiply = 1
        # for key in dic:
        #     multiply *= key
        # return (multiply + len(dic))
        rabbits = 0
        for ans, val in dic.items():
            rabbits += ((val + ans) //(ans + 1) * (ans + 1))
        return rabbits
            