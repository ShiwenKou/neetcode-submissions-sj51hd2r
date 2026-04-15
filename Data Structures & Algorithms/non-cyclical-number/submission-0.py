class Solution:
    def isHappy(self, n: int) -> bool:
        

        seen = set()


        def getRes(num):
            res = 0
            while num:
                cur = num % 10
                num = num // 10
                res += cur ** 2
            
            return res

        while True:

            res = getRes(n)
            if res == 1:
                return True
            if res in seen:
                return False
            seen.add(res)
            n = res