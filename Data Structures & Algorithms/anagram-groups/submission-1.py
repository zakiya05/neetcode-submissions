class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        for word in strs:
            x = [0]*26
            for i in word:
                x[ord(i) - ord('a')]+=1
            anagram_group[tuple(x)].append(word)
        return list(anagram_group.values())