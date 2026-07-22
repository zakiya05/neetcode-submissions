class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map=defaultdict(list)
        for word in strs:
            x=[0]*26
            for char in word:
                x[ord(char)-ord('a')]+=1
            group_map[tuple(x)].append(word)
        return list(group_map.values())