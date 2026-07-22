class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        for i in range(len(strs[0])):
            y = strs[0][i]
            print(y)
            for j in range(len(strs)):
                if len(strs[j])<=i:
                    return s
                print(y,i,j)
                if strs[j][i]!=y:
                    return s
            s+=y
        return s
                