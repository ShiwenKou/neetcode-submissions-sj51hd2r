class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # 我们有 [1, n + 1]找出来确实的positive

        # 我们可以用数组的index来标记 1 到n是否存在。 通过负数标记法。

        # 唯一一个edge case 如果每个数都是负数，那说明 n+1是不存在的


        for i in range(len(nums)):
            nums[i] = nums[i] + 1

        for i in range(len(nums)):
            val = abs(nums[i])

            if val <= len(nums):
                idx = val - 1
                nums[idx] = -abs(nums[idx])

        for i in range(len(nums)):

            if nums[i] > 0:
                return i
        return len(nums)