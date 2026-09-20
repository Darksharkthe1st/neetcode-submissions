class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        for c in s:
            if c == ')':
                if len(parens) == 0 or parens.pop() != '(':
                    return False
            elif c == ']':
                if len(parens) == 0 or parens.pop() != '[':
                    return False
            elif c == '}':
                if len(parens) == 0 or parens.pop() != '{':
                    return False
            else:
                parens.append(c)
        return len(parens) == 0
            