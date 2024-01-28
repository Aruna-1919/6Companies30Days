class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)   
        mod=10**9+7
        for i in range(k):
            heappush(nums,heappop(nums)+1)   
        product=1
        for i in nums:
            product=(product*i)%mod
        return product
