class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute: O(N^2)
        # op_mux =[]
        # for i in range(len(nums)):
        #     temp = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         temp *= nums[j]
        #     op_mux.append(temp)
        # return op_mux
        #DIVISION LOGIC:: not optimal: 
        # num_mux, zero_cnt = 1, 0

        # for i in nums:
        #     if i:
        #         num_mux *= i
        #     else:
        #         zero_cnt += 1

        # op =[0] * len(nums)
        # if zero_cnt > 1: 
        #     return op

        # for i, val in enumerate(nums):
        #     if zero_cnt:
        #         if val:
        #             op[i] = 0
        #         else:
        #             op[i] = num_mux
        #     else:
        #         op[i] = num_mux//val
        # return op

        # Best:pre postfix
        n = len(nums)
        res = [0]*n
        pre = [0]*n
        post = [0]*n
        pre[0] = post[n - 1] = 1

        for i in range(1, n): # for prefix array
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):# for postfix
            post[i] = post[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = pre[i] * post[i]
        return res
