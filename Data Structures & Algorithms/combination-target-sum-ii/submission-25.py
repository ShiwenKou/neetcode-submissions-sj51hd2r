class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sol = []
        def dfs(i, remaining):

            if remaining == 0:
                res.append(sol[:])
                return
            
            if i >= len(candidates) or remaining < 0:
                return

            sol.append(candidates[i])

            dfs(i + 1, remaining - candidates[i])

            sol.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, remaining)

        dfs(0, target)
        return res