class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c=0
        i=len(g)-1
        j=len(s)-1
        s.sort()
        g.sort()
        while i>=0 and j>=0:
            if g[i]<=s[j]:
                c=c+1 
                i-=1
                j-=1
            elif g[i]>s[j]:
                i-=1
        return c


        
