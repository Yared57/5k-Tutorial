class Solution:
    def maxArea(self, height: List[int]) -> int:
        MaxArea=0
        left=0
        right=len(height) - 1

        while(right>left):
            if (height[right]>height[left]):
                Area=(right-left)*height[left]
                left+=1
            else:
                Area=(right-left)*height[right]
                right-=1

            if(Area>MaxArea):
                MaxArea=Area
        return MaxArea                

        
