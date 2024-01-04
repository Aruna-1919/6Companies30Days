class Solution(object):
    
    def numberOfWays(self, startPos, endPos, k):
        """
        :type startPos: int
        :type endPos: int
        :type k: int
        :rtype: int
        """
        mod=10**9+7
        def fun(start,end,curr,k,dp):
            if k==0:
                if curr==end:
                    return 1
                else:
                    return 0
            if dp[curr][k]!=-1:
                return dp[curr][k]
            rightMove=fun(start,end,curr+1,k-1,dp)%mod
            leftMove=fun(start,end,curr-1,k-1,dp)%mod
            dp[curr][k]=(leftMove+rightMove)%mod
            return dp[curr][k]

        dp= [[-1 for _ in range(1001)] for _ in range(3002)]
        return fun(startPos,endPos,startPos,k,dp)
        
        



        
