class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        res = [0] * (len(num1) + len(num2))


        for i in range(len(num1) - 1, -1 , -1):
            for j in range(len(num2) - 1, -1, -1):

                mul = int(num1[i]) * int(num2[j])

                p1, p2 = i + j, i + j + 1
                total = res[p2] + mul
                res[p2] = total % 10

                res[p1] = res[p1] + total // 10

        result = ''.join(map(str, res)).lstrip('0')

        return result if result else '0'

