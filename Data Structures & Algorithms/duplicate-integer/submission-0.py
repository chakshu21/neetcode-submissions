class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: 
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
        nums_cnt = {}

        for i in range(len(nums)):
            if nums[i] in nums_cnt:
                return True
            nums_cnt[nums[i]]=1
        return False
