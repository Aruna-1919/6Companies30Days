from typing import List

class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        def findcount(prev, nums, visited, count):
            if count == len(nums):
                return 1

            result = 0
            for i in range(len(nums)):
                if visited[i]:
                    continue

                if (prev != -1 and nums[prev] % nums[i] != 0 and nums[i] % nums[prev] != 0):
                    continue

                visited[i] = True
                result = (result + findcount(i, nums, visited, count + 1)) % mod
                visited[i] = False 

            return result

        mod = pow(10, 9) + 7
        prev = -1
        visited = [False] * len(nums) 
        return findcount(prev, nums, visited, 0)
