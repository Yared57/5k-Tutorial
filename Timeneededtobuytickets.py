from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        Tracker=k
        Counter=0
        GG=deque(tickets)
        print(GG)
        while GG[Tracker]:
            if Tracker==0:
                GG[Tracker]-=1
                GG.append(GG.popleft())
                Counter+=1
                Tracker=len(tickets)-1
            elif(GG[0]):
                GG[0]-=1
                GG.append(GG.popleft())
                Counter+=1
                Tracker-=1
            else:
                GG.append(GG.popleft())
                Tracker-=1    
        return Counter        
