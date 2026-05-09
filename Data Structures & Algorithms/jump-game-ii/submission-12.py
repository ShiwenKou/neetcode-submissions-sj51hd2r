class Solution:
    def jump(self, nums: List[int]) -> int:
        
        left, right = 0, 0
        res = 0
        i = 0
        while right < len(nums) - 1:

            farthest = 0

            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

        
            right = farthest
            left = i + 1
            res += 1

        return res


            