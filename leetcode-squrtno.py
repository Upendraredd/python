class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        h=x
        if x==1:
            return 1
        for i in range(1000):
            mid=(l+h)//2
            if mid *mid ==x:
                return mid
            elif mid*mid<x:
                l =mid
            else:
                h =mid

        return l
