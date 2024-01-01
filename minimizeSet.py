import sys

class Solution(object):
    def gcd(self,d1,d2):
        if d2==0:
            return d1
        else:
            return self.gcd(d2,d1%d2)
    def check(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2,m,lcm):
        a = m - (m // divisor1)
        b = m - (m // divisor2)
        c = m - (m // divisor1) - (m // divisor2) +(m//lcm)
        if (a >= uniqueCnt1 and b >= uniqueCnt2 and a + b - c >= uniqueCnt1 + uniqueCnt2):
            return True
        else:
            return False


    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        l=1
        h=sys.maxsize
        ans=0
        lcm=(divisor1*divisor2)//self.gcd(divisor1,divisor2)
        while(l<=h):
            m=(l+h)//2
            if(self.check(divisor1, divisor2, uniqueCnt1, uniqueCnt2,m,lcm)):
                ans=m
                h=m-1
            else:
                l=m+1
        return ans
