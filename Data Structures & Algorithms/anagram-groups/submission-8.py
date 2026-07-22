class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rs= defaultdict(list)
        for s in strs:
            x=[0]*26
            for i in s:
                x[ord(i)-ord('a')]+=1
            rs[tuple(x)].append(s)
        return list(rs.values())