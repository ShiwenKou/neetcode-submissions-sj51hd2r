class Solution:
    def isHappy(self, n: int) -> bool:
        
        def helper(n):

            res = 0
            while n:

                digit = n % 10

                res += digit ** 2

                n = n // 10
            return res

    
        fast = helper(n)
        slow = n
        while fast != 1 and fast != slow:
            fast = helper(helper(fast))
            slow = helper(slow)
        
        return fast == 1