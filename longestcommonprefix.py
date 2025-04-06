class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
     acc = ""
     x = 0
     H = ""
     for i in strs: 
        if (x == 0 or x > len(i)):
            x = len(i)
            H = i
    
     for i in range(0, x, 1):
        for j in strs:
           
            if (H[i] != j[i]):
                return acc
            
        acc += j[i]
     return acc   
