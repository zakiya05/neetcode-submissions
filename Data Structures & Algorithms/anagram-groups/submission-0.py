class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            l = len(word)
            x=[0]*26
            for i in word:
                x[ord(i)- ord('a')]+=1
            anagram_map[tuple(x)].append(word)
        return list(anagram_map.values())