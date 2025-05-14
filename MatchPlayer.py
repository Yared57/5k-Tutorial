class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        One,Two=0,0
        Count=0
        while(One<len(players) and Two<len(trainers)):
            if(trainers[Two]>=players[One]):
                One+=1
                Two+=1
                Count+=1
            elif(trainers[Two]<players[One]):
                  Two+=1
        return Count          
