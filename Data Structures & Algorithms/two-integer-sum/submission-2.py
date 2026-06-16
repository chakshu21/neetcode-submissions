class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # BRUTE::
        # # for i in range(len(nums)):
        # #     for j in range(i+1,len(nums)):
        # #         if  nums[i]+nums[j] == target:
        # #             return [i,j]
        # # return []
        # #BEST::
        # mp = {}
        # for i in range(len(nums)):
        #     if target-nums[i] in mp:
        #         return [mp[target-nums[i]],i]
        #     mp[nums[i]]=i
        mp = {}

        for i in range(len(nums)):
            if target - nums[i] in mp:
                return [mp[target - nums[i]],i ]
            mp[nums[i]] = i