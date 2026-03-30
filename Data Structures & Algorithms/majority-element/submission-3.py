class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        from collections import defaultdict

        lst = defaultdict(int)

        for i in range(len(nums)):

            lst[nums[i]] += 1

        return max(lst, key=lst.get)