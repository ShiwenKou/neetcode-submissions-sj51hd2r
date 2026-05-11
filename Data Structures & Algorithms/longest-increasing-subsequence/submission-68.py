class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        tails = []

        def getFirstIndex(tails, n):

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
            idx = getFirstIndex(tails, n)

            if idx == len(tails):
                tails.append(n)
            
            else:
                tails[idx] = n
        return len(tails)
        
