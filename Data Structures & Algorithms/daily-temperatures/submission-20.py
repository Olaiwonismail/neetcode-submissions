class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        t = temperatures
        output = [0]*l
        stack = []
        
        
        for n,v in enumerate(t):
            if not stack:
                stack = [n]
                continue
            #  t[stack[-1]]
            if v <=  t[stack[-1]]:
                stack.append(n)
            else:
                while v >  t[stack[-1]]:
                    output[stack[-1]] = n-stack[-1] 
                    stack.pop()
                    if not stack:
                        break
            stack.append(n)
                    
        return output


            

            

        