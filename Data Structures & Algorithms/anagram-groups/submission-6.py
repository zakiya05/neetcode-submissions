class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            x=[0]*26
            for i in s:
                x[ord(i)-ord('a')]+=1
            d[tuple(x)].append(s)
        return list(d.values())