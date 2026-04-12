class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        

        nums = [1] + nums + [1]

        memo = {}


        def dfs(l, r):

            if l > r:
                return 0
            
            if (l, r) in memo:
                return memo[(l, r)]
            res = 0
            for i in range(l, r + 1): # 有这么多选择
            # 如果选i作为最后一个burst，那么我们就会有两个子问题要处理。
                res = max(res, nums[l - 1] * nums[i] * nums[r + 1] + dfs(l, i - 1) + dfs(i + 1, r))
                
            memo[(l, r)] = res
            return res

        return dfs(1, len(nums) - 2)