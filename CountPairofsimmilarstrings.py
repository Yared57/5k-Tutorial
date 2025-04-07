class Solution:
    def similarPairs(self, words: List[str]) -> int:
        x=len(words)
        Arr = [[0 for _ in range(10)] for _ in range(x)]
        II=0
        
        for i in words:
            JJ=0
            for j in i:
                if(j not in Arr[II]):
                    Arr[II][JJ]=j
                JJ+=1

            II+=1
        for i in Arr:

            while 0 in i:

                i.remove(0)
        xx=len(Arr)
        gg=0
        for i in Arr:
            i.sort()        
        for i in range(xx):
            for j in range(i+1,xx,1):
                if(Arr[i]==Arr[j]):
                
               
                    gg+=1
        print (Arr)
        return gg         
