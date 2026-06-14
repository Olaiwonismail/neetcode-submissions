class Solution:
    def isValid(self, s: str) -> bool:
        b = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        l =[]
        if len(s) <= 1:
            return False
        s = list(s)
        for x,item in enumerate(s):
            if item in b:
                if len(l) > 0:
                    if l[-1] == b[item]:
                        l.pop()
                        if len(l) == 0 and x == len(s)-1:
                            return True
                    else:
                        return False
                else:
                    return False
            else:
                l.append(item)
            
        return False
        

            
            