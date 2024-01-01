class Solution(object):
     def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        if (len(set(nums))==1 and len(nums)>1):
            return list(range(len(nums) ))
        l=nums
        ans=[]
        for i in range(len(queries)):
            t=queries[i][1]
            m=sorted(l,key=lambda x:x[-t:])
            ans.append(nums.index(m[queries[i][0]-1]))
            l=nums
      
        return ans
