class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # 999 * 999-> res -> 3 + 3 = 6
        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1 , -1):
            for j in range(n - 1, -1, -1):

                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j + 1, i + j
                total = res[p1] + mul

                res[p1] = total % 10

                res[p2] = res[p2] + total // 10
    
        result = ''.join(map(str, res)).lstrip('0')

        return result or '0'


