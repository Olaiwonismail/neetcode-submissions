class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m ={}
        top_n = k
        for num in nums:
            m[num] = m.get(num,0)+1
        #  item in order of how frequent they are 
        sorted_items = sorted(m.items(), key=lambda item: item[1])
        ans=[]
        for n in range(1,top_n+1):
            ans.append(sorted_items[-n][0])
            

        return ans

