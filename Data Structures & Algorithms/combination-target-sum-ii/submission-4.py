class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def dfs(cur, i, total):

            if total == target:
                res.append(cur[:])
                return

            if i >= len(candidates) or total > target:
                return
            

            cur.append(candidates[i])
            dfs(cur, i+1, total + candidates[i])
            cur.pop()

            while i + 1 < len(candidates) and candidates[i+ 1] == candidates[i]:
                i += 1
            dfs(cur, i + 1, total)
        res = []
        dfs([], 0, 0)
        return res