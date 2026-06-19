class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # loop thorouh each value
        # loop through other values to see if <
        ans =[]
        
        for i in range(len(temperatures)):
            val =0
            for j in range(i+1,len(temperatures)):
                if  temperatures[i] < temperatures[j]:
                    val = j-i
                    break
            ans.append(val)
        return ans



        