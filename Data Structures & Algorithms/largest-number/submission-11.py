class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        
        nums2 = [str(c) for c in nums]

        res =self.bubble(nums2)

        return str(int(''.join(res)))
        
    def bubble(self, lst):

        length = len(lst) - 1

        sort_flag = False

        while not sort_flag:

            sort_flag = True

            for i in range(length): # cannot take the last element

                if lst[i] + lst[i+1] < lst[i+1] + lst[i]:

                    lst[i+1], lst[i] = lst[i], lst[i+1]

                    sort_flag = False
        return lst


