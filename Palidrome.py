class Solution:
    def isPalindrome(self, x: int) -> bool:
        T=str(x)
        g=len(T)-1
        h=T[g::-1]
        if(h==T):
            return True
        else:
            return False    
