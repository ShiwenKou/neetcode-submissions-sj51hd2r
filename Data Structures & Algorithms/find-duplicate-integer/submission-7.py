class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast = 0 # since there is repeating numbers, so there must be cycle inside
        
        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow2 == slow:
                return slow