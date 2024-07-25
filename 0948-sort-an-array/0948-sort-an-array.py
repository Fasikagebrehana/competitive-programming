class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(lhalf, rhalf):
            ans = []
            l, r = 0, 0
            while l < len(lhalf) and r < len(rhalf):
                if lhalf[l] > rhalf[r]:
                    ans.append(rhalf[r])
                    r += 1
                else:
                    ans.append(lhalf[l])
                    l += 1
            ans.extend(lhalf[l:])
            ans.extend(rhalf[r:])
            return ans

        def helper(arr, l, r):
            if l == r:
                return [arr[l]]
            middle = (l + r) // 2
            left = helper(arr, l, middle)
            right = helper(arr, middle + 1, r)
            return merge(left, right)    
            
        return helper(nums, 0, len(nums) - 1)