class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ref ={
            '(':')',
            '[':']',
            '{':'}',
        }
        for c in s:
            if ref.get(c,0):
                stack.append(c)
            elif len(stack) > 0 and ref[stack[-1]] == c:
                stack.pop()
            else:
                return False

        return len(stack)==0