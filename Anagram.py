class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        temp=''
        win=len(p)
        anagram=[]
        print(target)
        for i in range(len(s)):
            temp=s[i:i+win]
            if(target==Counter(temp)):
                anagram.append(i)
        return anagram  
