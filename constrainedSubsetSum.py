from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        dq = deque()

        for i in range(n):
            if dq and dq[0] < i - k:
                dq.popleft()
            dp[i] = nums[i] + (dp[dq[0]] if dq else 0)
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            if dp[i] > 0:
                dq.append(i)
        return max(dp)
