class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = {}
        freq = [[] for i in range(len(nums)+1)]
        print(freq)
        for n in nums:
            ctr[n] = 1 + ctr.get(n,0)
        print(ctr)
        for key, val in ctr.items():
            freq[val].append(key)
        print(freq)
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res