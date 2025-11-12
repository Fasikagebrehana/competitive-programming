class Solution:
    def intToRoman(self, num: int) -> str:
        # what if we change the numebr to their multipliers
        # like 3749 = 3000 + 700 + 40 + 9
        # when to substract => if number starts with 4 or 9

        # store values of the roman values with their respective signs
        store = {1: 'I', 5: 'V', 10:'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        roman = [1, 5, 10, 50, 100, 500, 1000]

        nums = []
        multiplier = 1
        while num > 0:
            rem = num % 10
            num = num // 10
            nums.append(rem * multiplier)
            multiplier *= 10
        nums = nums[::-1]
        # print(nums)
        # ?? how to know which to choose
        # thinking of using binary search but it might be too much
        # is there any other way to find the corresponding number from store for each number inside nums
        answer = []
        for num in nums:
            i = bisect_left(roman, num)
            if i == len(roman):
                n = int(str(num)[0])
                answer.append('M' * n)
            elif str(num)[0] == '4' or str(num)[0] == '9':
                answer.append(store[roman[i]- num] )
                answer.append(store[roman[i]])
            else:
                # print(num)
                if num in roman:
                    answer.append(store[num])
                    continue
                summ = 0
                nn = num
                while summ < nn:
                    i = bisect_left(roman, num)
                    # print(i)
                    if num in roman:
                        answer.append(store[num])
                        num -= roman[i]
                        summ += roman[i]
                        continue
                    answer.append(store[roman[i-1]])
                    num -= roman[i-1]
                    summ += roman[i-1]
                    # print(summ)
        # print(answer)
        return ''.join(answer)
                