class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_indexes = []
        b_indexes = []
        # print(len(s))
        i = j = 0
        ptr1 = ptr2 = 0 #pointer at a and b
        while i < len(s):
            idx1 = i
            while ptr1 < len(a) and idx1 < len(s) and  s[idx1] == a[ptr1]:
                ptr1 += 1
                if ptr1 == len(a):
                    a_indexes.append(i)
                    break
                idx1 +=1
            ptr1 = 0
            idx2 = i
            while ptr2 < len(b) and idx2 < len(s) and s[idx2] == b[ptr2]:
                ptr2 += 1

                if ptr2 == len(b):
                    b_indexes.append(i)
                    break
                idx2 += 1
            
            ptr2 = 0
            i+=1
        # print(a_indexes, b_indexes)

        result = []
        for i in range(len(a_indexes)):
            for j in range(len(b_indexes)):
                # print(a_indexes[i], b_indexes[j])
                if abs(a_indexes[i] - b_indexes[j]) <= k:
                    result.append(a_indexes[i])
                    break
                    # print(a_indexes[i])
        return result