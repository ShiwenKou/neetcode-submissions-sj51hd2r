class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.nums = nums
        self.sol = []
        self.res = []
        self.dfs(0)
        return self.res
    
    def dfs(self, i):
        if i == self.n:
            self.res.append(self.sol[:])
            return
        self.sol.append(self.nums[i])
        self.dfs(i+1)

        self.sol.pop()
        self.dfs(i+1)


        
