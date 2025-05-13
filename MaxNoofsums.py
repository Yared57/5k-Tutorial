class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        count=0
        while(right>left):
            if(nums[right]+nums[left]>k):
                right-=1
            elif(nums[right]+nums[left]<k):
                left+=1
            else:
                right-=1
                left+=1
                count+=1
        return count   
