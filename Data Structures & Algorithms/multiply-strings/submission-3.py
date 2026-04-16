class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if '0' in [num1, num2]:
            return '0'
        num1, num2 = num1[::-1], num2[::-1]

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                digits = int(num1[i]) * int(num2[j])

                res[i + j] += digits
                res[i + j + 1] += res[i + j] // 10
                res[i + j] = res[i + j] % 10
        
        res = res[::-1]
        begin = 0
        while begin < len(res) and res[begin] == 0:
            begin += 1
        
        res = res[begin:]
        res = map(str, res)
        return ''.join(res)