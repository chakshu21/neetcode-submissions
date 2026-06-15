class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, ml = 0, 0, 0
        mp = {}
        while r < len(s):
            mp[s[r]] = 1 + mp.get(s[r],0)
            while (r-l+1) - max(mp.values()) > k:
                mp[s[l]] -= 1
                l += 1
            ml = max(ml,r-l+1)
            r += 1
        return ml