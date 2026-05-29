class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = [0] * len(digits)
        carry = 1
        for i in range(len(digits) - 1, -1, -1):

            val = digits[i] + carry
            carry = val // 10
            val = val % 10

            res[i] = val

        if carry:
            res.insert(0, carry)

        return res


