class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charset=set()
        res=0
        left=0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])    
            res=max(res,right-left+1)
        return res  
