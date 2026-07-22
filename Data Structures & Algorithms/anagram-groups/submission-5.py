class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            conv = [0]*26
            for char in word:
                conv[ord(char)-ord('a')]+=1
            res[tuple(conv)].append(word)
        return list(res.values())