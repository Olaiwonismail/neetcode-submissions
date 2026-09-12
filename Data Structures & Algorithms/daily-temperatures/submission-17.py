class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        t = temperatures
        output = [0]*l
        stack = []
        
        
        for n,v in enumerate(t):
            if not stack:
                stack = [[v,n]]
                continue
            val =  stack[-1][0]
            if v <= val:
                stack.append([v,n])
               
            else:
                while v > stack[-1][0]:
                    i=stack[-1][1]
                    output[i] =  n - i
                    stack.pop()
                    if not stack:
                        break
                stack.append([v,n])
                    
        return output


            

            

        