class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        m = {}

        for str_ in strs:
            s = tuple(sorted(str_))

            m[s] = m.get(s,[])
            m[s].append(str_)
        return list(m.values())
        