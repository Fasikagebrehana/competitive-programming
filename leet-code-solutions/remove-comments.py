class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        open_block_comment = "/*"
        close_block_comment = "*/"
        single_comment = "//"
        temp = []
        ans = []
        i = 0
        flag = False
        for string in source:
            i = 0
            while i < len(string):
                if not flag and string[i:i+2] == '//':
                    break
                elif not flag and string[i:i+2] == "/*":
                    flag = True
                    i += 1
                elif flag and string[i:i+2] == "*/":
                    flag = False
                    i += 1
                elif not flag:
                    temp.append(string[i])                   
                i += 1
            if not flag and temp:
                ans.append("".join(temp))
                temp = []
        return ans
