class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        sol = []
        candidates.sort() # 2,2,4,5,6,9
        def dfs(i, total):
            if total == target:
                res.append(sol[:])
                return

            if i >= len(candidates) or total > target:
                return
            
            sol.append(candidates[i])

            # we have two paths. we want this element in the left and we nv want it in the right paht
            # for exmaple, # 2,2,4,5,6,9, if we explore 2 in the left, we'd nv want it appear in the right path

            dfs(i + 1, total + candidates[i]) # here we use i + 1, cuz the problem says, each element may be choosen at most once

            # since we don't want 2 in the right path
            sol.pop()
            while i + 1 < len(candidates) and candidates[i + 1] == candidates[i]:
                i += 1
            dfs(i + 1, total) # we are guaranteed that candidates[i+1] is not equal to candidaites[i]
        dfs(0, 0)
        return res


