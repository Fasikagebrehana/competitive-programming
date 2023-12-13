class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        lis = []
        for i in range(len(boxes)):
            if boxes[i] == '1':
                lis.append(i)
        ans = [0] * len(boxes)  
        
        for i in range(len(boxes)):
            for j in range(len(lis)):
                ans[i] += abs(i - lis[j]) 
        return ans