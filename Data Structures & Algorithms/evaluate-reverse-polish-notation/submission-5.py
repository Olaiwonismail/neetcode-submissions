class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = ['+','-','*','/']
        t =[]
        base = int(tokens[0])
        length = len(tokens)
        for item in tokens:
            if item not in signs:
                t.append(int(item))
            else:
                x =int(t[-2])
                y = int(t[-1])
                if item=='+':
                    num = x+y
                    
                if item=='-':
                    num = x-y
                    
                if item=='*':
                    num = x*y
                    
                if item=='/':
                    num = x/y
                t.pop()
                t.pop()
                t.append(num)
        import math
        return math.ceil(int(t[0]))
