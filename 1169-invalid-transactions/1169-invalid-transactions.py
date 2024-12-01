class Solution:
    def invalidTransactions(self, nums: List[str]) -> List[str]:
        answer = set()
        dic = defaultdict(list)
        for i in range(len(nums)):
            a, b, c, d = nums[i].split(',')
            if int(c) > 1000:
                answer.add(i)

            for j in range(i+1,len(nums)):
                a2,b2,c2,d2=nums[j].split(",")
               
                if a==a2 and d2!=d and abs(int(b)-int(b2))<=60:
                    answer.add(i)
                    answer.add(j)


        

        res=[]
        for i in answer:
            res.append(nums[i])

        # print(answer)
        return res
            
        



            