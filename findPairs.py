class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0 

        nums = sorted(nums)
        set_a = set()
        seen = set()

        for i in range(len(nums)):
            if nums[i] - k in seen:
                set_a.add((nums[i] - k, nums[i]))

            seen.add(nums[i])
        return len(set_a)
