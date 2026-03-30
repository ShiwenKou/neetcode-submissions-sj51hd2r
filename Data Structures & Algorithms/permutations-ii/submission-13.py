class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        sol = []
        counter = collections.Counter(nums)

        def dfs():
            if len(nums) == len(sol):
                res.append(sol[:])
                return
            
            for n in counter:
                if counter[n] > 0:

                    counter[n] -= 1
                    sol.append(n)

                    dfs()

                    sol.pop()
                    counter[n] += 1
        dfs()
        return res

                
    