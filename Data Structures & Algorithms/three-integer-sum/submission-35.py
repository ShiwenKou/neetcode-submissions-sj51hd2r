class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                target = nums[i] + nums[left] + nums[right]

                if target > 0:
                    right -= 1
                elif target < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        return res