class Solution:
    def findRepeatedDnaSequences(self,s):
        d={}
        for i in range(len(s)-9):
            ss=s[i:i+10]
            if ss in d:
                d[ss]+=1
            else:
                d[ss]=1
        res=[x for x in d if d[x]>1]
        return res
        
