class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # 找到第一个大于等于

        tails = []

        def findLeft(tails, n):
            left, right = 0, len(tails) - 1
            res = len(tails) # if we cannot find such index 

            while left <= right:
                mid = (left + right) // 2

                if tails[mid] >= n:
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return res

        
        for n in nums:

            idx = findLeft(tails, n)
            if len(tails) == idx:
                tails.append(n)
            else:
                tails[idx] = n
        return len(tails)