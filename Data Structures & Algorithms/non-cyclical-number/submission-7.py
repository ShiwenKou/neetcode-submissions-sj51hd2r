class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(n):

            return sum(int(c) ** 2 for c in str(n))

        
        fast = helper(n)
        slow = n

        while fast != 1 and fast != slow:
            fast = helper(helper(fast))
            slow = helper(slow)

        return fast == 1