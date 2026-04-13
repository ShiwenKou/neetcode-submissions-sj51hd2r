class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 既然是连续，那他就是个partion 问题。处理了左边partition。右边就是个子问题。

        # def dfs(start):

        #     if start >= len(nums):
        #         return float('-inf')



        #     for end in range(start, len(nums)):
        #         res = 1
        #         for n in nums[start: end + 1]:
        #             res *= n
        #         res = max(res, dfs(end + 1))

        #     return res

        # return dfs(0)

        #上面的感觉好像不对。这似乎是个二维问题。像是palindrome那样的。或者说是个range问题

        memo = {}
        def dfs(i, j):
            if i == j:
                return nums[i]
            if i > j:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]

            
            res = nums[i]  * dfs(i + 1, j - 1) * nums[j]
            memo[(i, j)] = res
            return res

        ans = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                ans = max(ans, dfs(i, j))
        return ans



