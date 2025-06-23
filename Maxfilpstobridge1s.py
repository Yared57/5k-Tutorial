class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        right=0
        left=0
        Zerocounter=0
        Max=0
        if nums[0]==0:
            Zerocounter=1
        while right <len(nums):
            if(Zerocounter<=k):
                Max=max(Max,right-left+1)
                right+=1
                if right<len(nums) and nums[right]==0:
                        Zerocounter+=1
                    
            else:
                if nums[left]==0:
                    Zerocounter-=1 
                left+=1
            
        return Max  
