class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        tails = []

        def findFirst(tails, n):

            left, right = 0, len(tails) - 1
            res = len(tails)
            while left <= right:

                mid = (left + right) // 2

                if tails[mid] >= n:
                    res = mid
                    right = mid - 1

                else:
                    left = mid + 1

            return res

        
        for n in nums:

            index = findFirst(tails, n)

            if index == len(tails):
                tails.append(n)

            else:
                tails[index] = n

        return len(tails)