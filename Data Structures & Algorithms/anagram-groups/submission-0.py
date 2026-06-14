class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp =defaultdict(list)
        for i in strs:
            sort = ''.join(sorted(i))
            mp[sort].append(i)
        # print(mp)
        return list(mp.values())