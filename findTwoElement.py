class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        l=[]
        re= {key: 0 for key in range(1, n + 1)}
        for i in arr:
            re[i]+=1
        a=[key for key, value in re.items() if value == 0]
        b=[key for key, value in re.items() if value == 2]
        b.extend(a)
        
        return b

