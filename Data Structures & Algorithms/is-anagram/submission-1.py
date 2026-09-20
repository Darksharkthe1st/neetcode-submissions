class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen: dict = {}
        if (len(s) != len(t)):
            return False

        t = sorted(t)
        s = sorted(s)
        return s == t
        # for c in s:
        #     seen[c] = seen.get(c, 0) + 1

        # for c in t:
        #     if (seen.get(c, -1) <= 0):
        #         return False
        #     seen[c] = seen.get(c) -1
        # return True