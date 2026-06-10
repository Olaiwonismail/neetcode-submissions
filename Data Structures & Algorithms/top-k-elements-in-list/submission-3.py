class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m ={}
        for item in nums:
            m[item] = m.get(item,0)+1
        bucket = [[] for _ in range(len(nums)+1)]
        for key,val in m.items():
            bucket[val].append(key)
        ans = []
        for item in bucket[::-1]:
            ans.extend(item)
            if len(ans) >= k:
                return ans[:k]
        # cutoff=sorted(m.values())
        # cutoff = cutoff[-k]
        # for key,val in m.items():
        #     if val >= cutoff:
        #         ans.append(key)
        # return ans

        