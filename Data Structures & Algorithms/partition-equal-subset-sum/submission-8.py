class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        def dfs(i, remaining):
            if remaining == 0:
                return True

            if i >= len(nums) or remaining < 0:
                return False

            res = dfs(i + 1, remaining - nums[i]) or dfs(i + 1, remaining) # no

            return res
        
        return dfs(0, target)