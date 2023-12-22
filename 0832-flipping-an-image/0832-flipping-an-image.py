class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            # n = 0
            # m = len(image) - 1
            # while n < m:
            #     image[i][n], image[i][m] = image[i][m], image[i][n]
            #     n += 1
            #     m -= 1
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image