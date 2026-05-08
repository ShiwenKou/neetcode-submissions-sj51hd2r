class Solution:
    def isHappy(self, n: int) -> bool:
        


        def helper(n):

            return sum(int(num) ** 2 for num in str(n))

        
        slow = n
        fast = helper(n)

        while fast != 1:

            slow = helper(slow)
            fast = helper(helper(fast))
            if fast == slow:
                return False

        return True