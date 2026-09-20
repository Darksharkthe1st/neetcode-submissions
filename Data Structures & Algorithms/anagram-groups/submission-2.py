class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sorty = "".join(sorted(s))
            groups[sorty] = groups.get(sorty, [])
            groups[sorty].append(s)
        
        output = []
        for k,v in groups.items():
            output.append(v)
        
        return output