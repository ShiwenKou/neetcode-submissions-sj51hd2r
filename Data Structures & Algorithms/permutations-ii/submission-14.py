class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        sol = []
        count = collections.Counter(nums)

        def dfs():
            if len(nums) == len(sol):
                res.append(sol[:])
                return        
            
            for n in count:
                if count[n] > 0:
                    count[n] -= 1
                    sol.append(n)

                    dfs()

                    sol.pop()
                    count[n] += 1
        dfs()
        return res