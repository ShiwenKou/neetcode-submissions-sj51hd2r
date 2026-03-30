class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        sol = []
        counters = collections.Counter(nums)

        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for n in counters:
                if counters[n] > 0:

                    sol.append(n)
                    counters[n] -= 1

                    dfs()

                    counters[n] += 1
                    sol.pop()
        dfs()
        return res
        