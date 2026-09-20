class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            alphaKey = [0] * 26
            for c in s:
                alphaKey[ord(c) - ord('a')] += 1
            alphaKey = tuple(alphaKey)
            groups[alphaKey] = groups.get(alphaKey, [])
            groups[alphaKey].append(s)
        
        output = []
        for k,v in groups.items():
            output.append(v)
        
        return output