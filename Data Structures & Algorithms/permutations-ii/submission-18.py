class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        cnt = collections.Counter(nums)
        res = []
        sol = []

        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return

            for n in cnt: # each time we can choose as long as the key has a value greater than 0
                if cnt[n] > 0:
                    sol.append(n)
                    cnt[n] -= 1

                    dfs()

                    sol.pop()
                    cnt[n] += 1
        dfs()
        return res