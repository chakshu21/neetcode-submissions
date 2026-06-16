class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # st = {}
        # # for i in nums:
        # #     if i in st:
        # #         return True
        # #     st[i]= True
        # # return False
        # return (len(set(nums))<len(nums))
        st  = set(nums)
        if len(st) != len(nums):
            return True
        # else:
        return False
