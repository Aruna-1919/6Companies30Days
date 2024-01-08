class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=sorted(nums)
        a=k[len(k)//2]
        n=0
        for i in k:
            n=n+abs(i-a)
        return n
        
