class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        memo = {}
        def dfs(i, remaining):
            if remaining == 0:
                return True
            if i >= len(nums) or remaining < 0:
                return False
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            res = dfs(i + 1, remaining - nums[i]) or dfs(i + 1, remaining)

            memo[(i, remaining)] = res
            return res

        return dfs(0, target)