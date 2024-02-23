class Solution:
    def minFlips(self, target: str) -> int:
        count=0

        flip=False
        for i in range(len(target)):
            if flip==False:
                if target[i]!='0':
                    count+=1
                    flip= True

            else:
                if target[i]=='0':
                    count+=1
                    flip=False
        return count