class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # frequency array
        # mp =defaultdict(list)
        # for i in strs:
        #     sort = ''.join(sorted(i))
        #     mp[sort].append(i)
        # # print(mp)
        # return list(mp.values())
        #using HASH Table 
        mp =defaultdict(list)
        for ss in strs:
            count = [0]*26
            for i in ss:
                count[ord(i)-ord('a')] +=1
            mp[tuple(count)].append(ss)
        return list(mp.values())