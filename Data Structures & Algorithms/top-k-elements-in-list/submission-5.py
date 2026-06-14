class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # mp = defaultdict()
        # for i in nums:
        #     mp[i] = 1 + mp.get(i,0)
        # res = []
        # for key,value in mp.items():
        #     if value >= k:
        #         res.append(key)
        # return res
        # bs = []*len(nums)
        # for i in nums:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res


