class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        res = []
        sol = []
        seen = set()
        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return


            for n in nums:
                if n not in seen:
                    sol.append(n)
                    seen.add(n)
                    dfs()
                    seen.remove(n)
                    sol.pop()
        dfs()
        return res