class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles.reverse()
        Alice=0
        You=1
        Bob=len(piles)-1
        sums=0
        print(piles)
        while(You<Bob):
            sums+=piles[You]
            You+=2
            Alice+=2
            Bob-=1
        return sums
