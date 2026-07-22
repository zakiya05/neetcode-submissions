class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)
        for word in strs:
            curr_g=[0]*26
            for char in word:
                curr_g[ord(char)-ord('a')]+=1
            anagram_group[tuple(curr_g)].append(word)
        return [val for val in anagram_group.values()]