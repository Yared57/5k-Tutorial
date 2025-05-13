class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        One=0
        Two=0
        while(One <len(nums1) and Two<len(nums2)):
            if(nums1[One]==nums2[Two]):
                return nums1[One]
            elif(nums1[One]>nums2[Two]):
                Two+=1
            else:
                One+=1
        return -1            
