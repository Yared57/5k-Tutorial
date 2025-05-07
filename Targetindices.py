class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        List1=[]
        for i in range(len(nums)):
            if(nums[i]==target):
                List1.append(i)
        return List1
