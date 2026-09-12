class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        t = temperatures
        output = [0]*l
        stack = []
        # m ={}
        # for n in range(0,l):
        #     m[temp[n]] = n
        
        for n in range(0,l):
            item  = t[n]

            if not stack:
                stack = [[item,n]]
                continue
            
            if item <= stack[-1][0]:
                stack.append([item,n])
               
            else:
                while item > stack[-1][0]:
                    output[stack[-1][1]] =  n - stack[-1][1]
                    stack.pop()
                    if not stack:
                        break
                stack.append([item,n])
                    
        return output


            

            

        