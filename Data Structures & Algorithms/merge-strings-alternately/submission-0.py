class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i1,i2=0,0
        j1,j2 = len(word1), len(word2)
        s= ""
        while i1<j1 and i2<j2:
            s+=word1[i1]+word2[i2]
            i1+=1
            i2+=1
        if i1<j1:
            s+=word1[i1:j1]
        if i2<j2:
            s+=word2[i2:j2]
        return s
