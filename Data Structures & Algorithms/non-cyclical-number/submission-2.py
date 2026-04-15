class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getRes(num):
            return sum(int(c) ** 2 for c in str(num))
        
        slow, fast = n, getRes(n)


        while fast != 1 and fast != slow:

            fast = getRes(fast)
            fast = getRes(fast)
            slow = getRes(slow)

        return fast == 1
            
            