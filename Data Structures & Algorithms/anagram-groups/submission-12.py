class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=defaultdict(list)
        for i in range(len(strs)):
            y=[0]*26
            for j,num in enumerate(strs[i]):
                y[ord(num)-ord('a')]+=1
            a[tuple(y)].append(strs[i])
                
        return list(a.values())