class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Max=float('-inf')
        NK=k-1
        sums=0
        for i in range(0,k,1):
            sums+=nums[i]
            Max=sums
        left=0
        print(sums)   
        for right in range(NK+1,len(nums),1):
            sums-=nums[left]
            sums+=nums[right]
            left+=1 
            if sums>Max:
                Max=sums
               
        return Max/k  
