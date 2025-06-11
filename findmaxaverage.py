class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums=0
        Max=float('-inf')
        for i in range(k):
            sums+=nums[i]
            Max = sums

        for i in range(1,len(nums)-k+1):
            sums=sums-nums[i-1]+nums[i+k-1]
            if(sums>Max):
                Max=sums
        return Max/k   
