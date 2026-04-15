class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carrier = 0
        res = [1] * len(digits)
        for i in range(len(digits) - 1, -1, -1):

            if i == len(digits) - 1:
                cur =  digits[i] + 1 + carrier
            else:
                cur = digits[i] + carrier
            carrier = cur // 10
            cur = cur % 10

            digits[i] = cur
        if carrier:
            digits.insert(0, carrier)
        return digits