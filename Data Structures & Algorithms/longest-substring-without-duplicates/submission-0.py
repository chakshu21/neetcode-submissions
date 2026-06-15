class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cset = set()
        ml = 0
        for r in range(len(s)):
            while s[r] in cset:
                cset.remove(s[l])
                l += 1
            cset.add(s[r])
            ml = max(ml,r-l+1)
        return ml

