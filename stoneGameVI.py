class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        arr=[(a+b,i) for i,(a,b) in enumerate(zip(aliceValues,bobValues))]
        arr.sort(reverse=True)
        p1=sum(aliceValues[v[1]] for i,v in enumerate(arr) if i%2==0)
        p2=sum(bobValues[v[1]] for i,v in enumerate(arr) if i%2==1)
        if p1>p2:
            return 1
        if p2>p1:
            return -1
        return 0
