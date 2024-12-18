class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False if n > 0 else True
            else:
                if n == 0:
                    return True
                elif n == 1 and flowerbed[0] == 0:
                    return True
                return False
        count = 0
        count1 = 0
        count2 = 0
        zero = False
        for i in range(1, len(flowerbed), 2):
            if i == len(flowerbed) - 1:
                if flowerbed[i-1] != 1 and flowerbed[i] == 0:
                    count1 += 1
            elif flowerbed[i-1] != 1 and flowerbed[i+1] != 1 and flowerbed[i] == 0:
                count1 += 1


        for i in range(0, len(flowerbed), 2):
            if i == 0:
                if flowerbed[i+1] != 1 and flowerbed[i] == 0:
                    count2 += 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i-1] != 1 and flowerbed[i] == 0:
                    count2 += 1
            elif flowerbed[i-1] != 1 and flowerbed[i+1] != 1 and flowerbed[i] == 0:
                count2 += 1

            
        # print(count1, count2)
        count = max(count1, count2)
        if count >= n:
            return True
        return False