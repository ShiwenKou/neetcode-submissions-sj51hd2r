class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        used = set()

        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for n in nums:
                if n not in used:
                    sol.append(n)
                    used.add(n)

                    dfs()

                    used.remove(n)
                    sol.pop()
        dfs()
        return res