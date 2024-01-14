class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        ans=0
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                if nums2[j-1]==nums1[i-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                    ans=max(ans,dp[i][j])
        return ans
        
