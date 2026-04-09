class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        total = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums) -1, -1, -1):
            newDP = set()
            for n in dp:
                newDP.add(n + nums[i])
                newDP.add(n)

            dp = newDP
        if total in dp:
            return True
        else:
            return False