class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m ={}
        
        
        for item in strs: 
            val = ''.join(sorted(item))    
            m[val] = m.get(val,[])
            m[val].append(item)
        return list(m.values())
            

                
        