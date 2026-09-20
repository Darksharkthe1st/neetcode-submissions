class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, list[str]] = {}
        for s in strs:
            sp = str(sorted(s))
            if sp in groups:
                groups[sp].append(s)
            else:
                groups[sp] = [s]
        result = []
        for grp in groups:
            result.append(groups[grp])
        return result