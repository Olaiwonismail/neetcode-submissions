class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return 'kk'
        s = 'hentai'.join(strs)
        
        return s

    def decode(self, s: str) -> List[str]:
        if s == 'kk':
            return []
        strs= s.split('hentai')
        return strs

