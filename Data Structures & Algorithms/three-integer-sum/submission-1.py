class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        op = []
        n =len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    op.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
        return op
            





































# BRUTE FORCE::
        # nums.sort()
        # n = len(nums)
        # op = set()
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 op.add(tuple([nums[i],nums[j],nums[k]]))
        # return [list(i) for i in op]