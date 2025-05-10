class Solution:
    def reverseVowels(self, s: str) -> str:
        right=len(s)-1
        left=0
        Vowles=['A','E','I','O','U','a','e','i','o','u']
        L1=list(s)
        print(L1)
        while(right>left):
            if(L1[left] in Vowles and L1[right] not in Vowles):
                right-=1
            elif(L1[left] not in Vowles and L1[right] in Vowles):
                left+=1
            elif(L1[left] in Vowles and L1[right] in Vowles):
                L1[left],L1[right]=L1[right],L1[left]
                left+=1
                right-=1
            else:
                left+=1
                right-=1    
        S2="".join(L1)
        return S2   
