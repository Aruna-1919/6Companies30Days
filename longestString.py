class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x==y:
            return x*2+y*2+z*2
        elif x<y:
            return x*4+2+z*2
        else:
            return y*4+2+z*2
        
