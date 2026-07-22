class Solution:
    def longestPalindrome(self, s: str) -> str:
        s= "#" + "#".join(s) +"#"
        longest_substring = ""
       
        for i in range(1,len(s)-1):
            j = 1
            
            cur_longest = ""
            while  i+j<len(s) and i-j>=0 and s[i-j] == s[i+j]:
                cur_longest = s[i-j : i+j+1]  
                j+=1
            if len(cur_longest)> len(longest_substring):
                longest_substring = cur_longest
        return longest_substring.replace("#","")




