class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sol = []
        seen = set()
        def dfs():
            for n in nums:
                if len(nums) == len(sol):
                    res.append(sol[:])
                    return
                
                if n not in seen:
                    sol.append(n)
                    seen.add(n)

                    dfs()

                    sol.pop()
                    seen.remove(n)
        dfs()
        return res

