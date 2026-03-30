class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []
        def dfs():
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for n in nums:
                if n not in curr:
                    curr.append(n)
                    dfs()
                    curr.pop()
        dfs()
        return res


            

        