class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        my=[]
        sq=[]
        res=[]
        for i in range(len(s)):
            if i+len(a)<=len(s) and s[i:i+len(a)]==a:
                my.append(i)
        for i in range(len(s)):
            if s[i:i+len(b)]==b:
                sq.append(i)
        for i in my:
            for j in sq:
                if abs(i-j)<=k:
                    res.append(i)
                    break
        print(my,sq,res)
        return res

        
