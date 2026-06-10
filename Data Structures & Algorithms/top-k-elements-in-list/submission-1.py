class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m ={}
        ans=[]
        for item in nums:
            m[item] = m.get(item,0)+1
        cutoff=sorted(m.values())
        cutoff = cutoff[-k]
        for key,val in m.items():
            if val >= cutoff:
                ans.append(key)
        return ans

        