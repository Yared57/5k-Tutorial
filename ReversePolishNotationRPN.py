class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in ["+","-","*","/"]:
                stack.append(int(i))
            elif i=="+":
                G=stack.pop()+stack.pop()
                stack.append(G)
            elif i=="-":
                S1=stack.pop()
                S2=stack.pop()
                stack.append(S2-S1)
            elif i=="*":
                G=stack.pop()*stack.pop()
                stack.append(G)
            elif i=="/":
                S1=stack.pop()
                S2=stack.pop()
                stack.append(int(S2/S1))
        return stack[0]                    

        
