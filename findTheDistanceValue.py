class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        c=0
        for i in arr1:
            if all([abs(i-arr2[j])>d for j in range(len(arr2))]):
                c=c+1
        print(c)
        return c
        
