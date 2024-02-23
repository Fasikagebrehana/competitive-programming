class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        ans = []
        stack.append(nums2[0])
        for i in range(1,len(nums2)):
            if nums2[i] < stack[-1]:
                stack.append(nums2[i])
            else:
                while stack and nums2[i] >= stack[-1]:
                    curr = stack.pop()
                    dic[curr] = nums2[i]
                stack.append(nums2[i])
                
        for i in range(len(nums1)):
            if nums1[i] in dic:
                ans.append(dic[nums1[i]])
            else:
                ans.append(-1)
        return ans