class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        P1=m-1
        P2=n-1
        Current=len(nums1)-1
        while P1>=0 and P2>=0:

            if(nums1[P1]>nums2[P2]):
                nums1[Current]=nums1[P1]
                P1-=1
                Current-=1
            else:
                nums1[Current]=nums2[P2] 
                P2-=1
                Current-=1
        while P2>=0:
            nums1[Current]=nums2[P2]
            P2-=1
            Current-=1        
