class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = [0] * len(prices)
        for i in range(len(prices)):
            j = i+1
            while j < len(prices):
                if prices[j] <= prices[i]:
                    answer[i] = prices[i] - prices[j]
                    break
                j += 1
            else:
                answer[i] = prices[i]
            
        
        
        # print(answer)
        return answer