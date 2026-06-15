class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l = 0
        # cset = set()
        # ml = 0
        # for r in range(len(s)):
        #     while s[r] in cset:
        #         cset.remove(s[l])
        #         l += 1
        #     cset.add(s[r])
        #     ml = max(ml,r-l+1)
        # return ml
        l, r, ml = 0, 0, 0
        mp = {}
        while r <len(s):
            if s[r] in mp:
                l = max(mp[s[r]]+1,l)
            mp[s[r]] = r
            r += 1
            ml = max(ml,r-l)

        return ml