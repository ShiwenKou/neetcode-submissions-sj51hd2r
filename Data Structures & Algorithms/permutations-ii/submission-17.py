class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums) 

        # {1:2,2:1}

        res = []
        sol = []
        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            

            for n in counter.keys():

                if counter[n] > 0:

                    sol.append(n)
                    counter[n] -= 1

                    dfs()

                    counter[n] += 1
                    sol.pop()
        
        dfs()
        return res