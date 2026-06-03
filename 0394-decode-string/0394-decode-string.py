class Solution:
    def decodeString(self, s: str) -> str:
        queue = deque()
        curr = 0
        i = len(s) - 1
        while i >= 0:
            if s[i].isdigit():
                # we have to collect all the digits since it can be 2 or 3 digit
                j = i
                while j >= 0 and s[j].isdigit():
                    j -= 1
                num = int(s[j+1:i+1])  # e.g. "11"
                i = j

                curr = ""
                while queue:
                    temp = queue.popleft()
                    if temp == '[':
                        continue
                    if temp == ']':
                        queue.appendleft(curr * num)
                        # print(queue, curr)
                        break
                    elif temp != '[':
                        curr += temp
            else:
                queue.appendleft(s[i])
                i -= 1
        # print(queue)

        answer = ''.join(queue)
        # print(answer)
        return answer