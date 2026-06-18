class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strs:
            # sorteds = ''.join(sorted(s))
            sorteds = [0]*26
            for i in range(len(s)):
                sorteds[ord(s[i])-ord('a')] += 1
            mp[tuple(sorteds)].append(s)
        return list(mp.values()) 