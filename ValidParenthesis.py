class Solution:
    def isValid(self, s: str) -> bool:
        Push={'(','{','['}
        Pop={')','}',']'}
        stack=[]
        boolr=True
        for i in s:
            if i in Push:
                stack.append(i)
            elif len(stack)!=0:
                top=stack.pop()
                if top+i in ["()","[]","{}"]:
                    continue
                else:
                    boolr=False
            else:
                boolr=False
        if len(stack)!=0 and stack.pop() in ["[","(","{"]:
            return False                
        return boolr   
