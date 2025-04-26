class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        sample=words[0]
        print(sample)
        w=[]
        for i in sample:
            flagged=True
            for j in words:
                if(i not in j):
                    flagged=False
            if(flagged):        
                w.append(i)
                words = [word.replace(i, '', 1) for word in words]    
        return w   
