class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        d={}
        for i in secret:
            n=int(i)
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        a=0
        b=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                a=a+1
        for i in guess:
            j=int(i)
            if j in d and d[j]>=1:
                b=b+1
                d[j]=d[j]-1
        s=str(a)+"A"+str(b-a)+"B"
        return s

        
