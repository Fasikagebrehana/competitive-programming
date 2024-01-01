class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookie = 0
        childcontent = 0
        while cookie < len(s) and childcontent < len(g):
            if s[cookie] >= g[childcontent]:
                childcontent += 1
            cookie += 1
        return childcontent
        