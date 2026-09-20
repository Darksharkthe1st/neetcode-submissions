class Solution:

    def encode(self, strs: List[str]) -> str:
        output: str = ""
        for s in strs:
            output += s + "å"
        return output
    
    def decode(self, s: str) -> List[str]:
        output: List[str] = []
        curr: str = ""
        for c in s:
            if c == "å":
                output.append(curr)
                curr = ""
            else:
                curr = curr + c
        return output