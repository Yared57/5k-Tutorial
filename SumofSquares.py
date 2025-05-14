class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a=0
        b=int(c**0.5)
        while(a<=b):
            if(a**2+b**2==c):
                return True
            elif(a**2+b**2<c):
                a+=1
            else:
                b-=1
        return False     
