class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        cnt = collections.Counter(nums)
        sol = []
        res = []
        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for n in cnt:
                if cnt[n] > 0:
                    cnt[n] -= 1
                    sol.append(n)
                    dfs()
                    cnt[n] += 1
                    sol.pop()
        dfs()
        return res
        