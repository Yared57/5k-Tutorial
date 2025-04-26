class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        Finallist=[0]*len(nums)
        for i in range(len(nums)):
            minnum=0
            for j in range(len(nums)):
                if(nums[i]>nums[j]):
                    minnum+=1
            Finallist[i]=minnum
        return Finallist            
        
