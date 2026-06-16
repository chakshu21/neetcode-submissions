class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # s1,t1 = {}, {}
        # for i in range(len(s)):
        #     s1[s[i]] = 1 + s1.get(s[i],0)
        #     t1[t[i]] = 1 + t1.get(t[i],0)
        # return s1 == t1
        if len(s) != len(t):
            return False
        sm, tm ={}, {}
        for i in range(len(s)):
            sm[s[i]] = 1 + sm.get(s[i],0)
            tm[t[i]] = 1 + tm.get(t[i],0)
        
        return sm == tm