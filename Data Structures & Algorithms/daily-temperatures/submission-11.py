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
            val =  stack[-1][0]
            if item <= val:
                stack.append([item,n])
               
            else:
                while item > stack[-1][0]:
                    i=stack[-1][1]
                    output[i] =  n - i
                    stack.pop()
                    if not stack:
                        break
                stack.append([item,n])
                    
        return output


            

            

        