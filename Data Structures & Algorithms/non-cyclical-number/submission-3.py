class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getRes(num):
            return sum(int(c) ** 2 for c in str(num))

        
        slow = n
        fast = getRes(n)

        while fast != 1 and slow != fast:
            slow = getRes(slow)
            fast = getRes(getRes(fast))
        
        return fast == 1