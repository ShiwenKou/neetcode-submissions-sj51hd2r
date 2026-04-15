class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getRes(num):
            return sum(int(c) ** 2 for c in str(num))
        
        slow, fast = n, getRes(n)


        while True:

            fast = getRes(fast)
            fast = getRes(fast)
            slow = getRes(slow)
            if fast == 1:
                return True
            if fast == slow:
                return False
            
            