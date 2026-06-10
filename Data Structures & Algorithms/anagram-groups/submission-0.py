class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # m ={}
        # ans =[]
        # for item in strs:
        #     if item in
        top = []
        low = []
        for item in strs:
            for xitem in strs:
                if sorted(item) == sorted(xitem):
                    if xitem not in [item for sublist in top for item in sublist]:
                        low.append(xitem)
            if low:
                top.append(low)
            low = []
        return top
