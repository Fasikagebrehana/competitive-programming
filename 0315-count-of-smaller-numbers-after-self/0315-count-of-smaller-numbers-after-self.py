class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergesort(num):
            if len(num) <= 1:
                return num
            middle = len(num) // 2
            left = mergesort(num[:middle])
            right = mergesort(num[middle:])

            return merge(left, right)
         
        def merge(leftHalf, rightHalf):
            l, r = 0, 0
            arr = []
            while l < len(leftHalf) or r < len(rightHalf):
                if r == len(rightHalf) or (l < len(leftHalf) and leftHalf[l][1] <= rightHalf[r][1]):
                    ans[leftHalf[l][0]] += r
                    arr.append(leftHalf[l])
                    l += 1
                else:
                    arr.append(rightHalf[r])
                    r += 1
            return arr
        
        ans = [0] * len(nums)
        num = list(enumerate(nums))
        mergesort(num)
        return ans