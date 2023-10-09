class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new=""
        begin=0
        for i in spaces:
            new+= s[begin:i] + " "
            begin = i
        new+= s[begin:]
        
        return new