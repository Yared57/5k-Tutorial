class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        One=0
        Two=0
        while(One <len(nums1) or Two<len(nums2)):
            if(One==len(nums1)-1):
                Two+=1
                if(nums1[One]==nums2[Two]):
                    return nums1[One]
            elif(Two==len(nums1)-1):
                One+=1
                if(nums1[One]==nums2[Two]):
                    return nums1[One]        
            elif(nums2[Two]>nums1[One]):
                One+=1
                if(nums1[One]==nums2[Two]):
                    return nums1[One]
            elif(nums2[Two]<nums1[One]):
                Two+=1
                if(nums1[One]==nums2[Two]):
                    return nums1[One]                  
                

    
        
