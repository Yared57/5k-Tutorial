class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        right=len(skill)-1
        left=0
        Skills=skill[len(skill)-1]+skill[0]
        print(skill)
        chemistry=0
        while(right>left):
            if(skill[right]+skill[left]==Skills):
                chemistry+=skill[right]*skill[left]
                right-=1
                left+=1
                

            else:
                return -1 
        return chemistry           
