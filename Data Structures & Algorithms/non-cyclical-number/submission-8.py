class Solution:
    def isHappy(self, n: int) -> bool:
        


        def helper(n):

            return sum(int(c) ** 2 for c in str(n))

        

        slow = n
        fast = helper(n)

        while fast != 1 and fast != slow:
            fast = helper(helper(fast))
            slow = helper(slow)

        return fast == 1