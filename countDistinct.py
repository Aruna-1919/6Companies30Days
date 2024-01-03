class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)                        
        arr = set()
        
        for start in range(n):
            cnt = 0
            tmp = ''
            for i in range(start, n):
                if nums[i]%p == 0:
                    cnt+=1                 
                tmp+=str(nums[i]) + ','        
                if cnt>k: 
                    break
                arr.add(tmp)                                    
                
        return len(arr)
