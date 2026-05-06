class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        goalPole = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goalPole:
                goalPole = i
            
        
        return True if goalPole == 0 else False