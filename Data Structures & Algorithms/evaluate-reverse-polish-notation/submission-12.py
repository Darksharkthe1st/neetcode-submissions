class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokStack: list[int] = []
        x: int = 0
        y: int = 0
        for t in tokens:
            if (t == '+'):
                y = tokStack.pop()
                x = tokStack.pop()
                tokStack.append(x + y)
            elif (t == '-'):
                y = tokStack.pop()
                x = tokStack.pop()
                tokStack.append(x - y)
            elif (t == '*'):
                y = tokStack.pop()
                x = tokStack.pop()
                tokStack.append(x * y)
            elif (t == '/'):
                y = tokStack.pop()
                x = tokStack.pop()
                if (abs(x) < abs(y) or y == 0): # Fix weird issue with python int division
                    tokStack.append(0)
                    continue
                
                sign = int((x//y) / (x//y))
                tokStack.append(int(x/y))
            else:
                tokStack.append(int(t))
            print(f"{x}{t}{y}={tokStack[-1]}")
        return int(tokStack[-1])