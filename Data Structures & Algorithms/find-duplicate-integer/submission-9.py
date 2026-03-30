class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # using index as node, and elements as next node, there are element appears two or more times, so there is definitely a cycle inside

        slow, fast = 0, 0

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0

        while True:
            slow = nums[slow]
            slow2= nums[slow2]
            if slow == slow2:
                return slow