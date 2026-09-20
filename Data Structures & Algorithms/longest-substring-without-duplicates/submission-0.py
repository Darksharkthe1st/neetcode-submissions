class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        lefty = 0
        righty = 0
        maxLen = 0
        while righty < len(s):
            # print(seen, lefty, righty)
            while s[righty] in seen:
                seen.remove(s[lefty])
                lefty += 1
            seen.add(s[righty])
            righty += 1
            maxLen = max(righty - lefty, maxLen)
        
        return maxLen