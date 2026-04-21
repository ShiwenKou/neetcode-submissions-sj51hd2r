class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 我的 所有index的范围是 0到len(nums) - 1:
        # 这说明我的idx 可以给 1 到 n进行标记的。
        # 如果是0的话我就不能标记了

        for i in range(len(nums)):
            nums[i] = nums[i] + 1


        for i in range(len(nums)):
            val = abs(nums[i])
            if val <= len(nums):
                idx = val - 1
                nums[idx] = abs(nums[idx]) * -1

        for i in range(len(nums)):

            if nums[i] > 0:
                return i
        return len(nums)