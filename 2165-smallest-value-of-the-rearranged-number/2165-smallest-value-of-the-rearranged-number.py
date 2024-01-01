class Solution:
    def smallestNumber(self, num: int) -> int:
        n = str(num)
        # print(n)
        # sorted_n = ''.join(sorted(n))
        if num >= 0:
            sorted_n = sorted(n)
            for i in range(len(sorted_n)):
                if sorted_n[i] != '0':
                    if i != 0:
                        sorted_n[0], sorted_n[i] = sorted_n[i], sorted_n[0]
                    break
            return int(''.join(sorted_n))
        else:
            sorted_num = sorted(n[1:], reverse=True)
            return int('-' + ''.join(sorted_num))