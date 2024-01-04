class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        mod=10**9+7

        l = [0] * (n + 1)
        l[1] = 1
        c = 0
        k=0
        for i in range(2, n + 1):
            nok=l[max(i-delay,0)]
            nof=l[max(i-forget,0)]
            c=c+nok-nof
            l[i]=c
        for i in range(n-forget+1,n+1):
            k=k+l[i]
        k=k%mod
        return k
