class Solution:
    def largestNumber(self, nums: List[int]) -> str:



        res = [str(c) for c in nums]

        ans = self.bubble(res)

        return str(int(''.join(ans)))

    def bubble(self, lst):
        flag_sort = False

        while not flag_sort:

            flag_sort = True

            for i in range(len(lst) - 1): # we don't want it to iterate to the last element

                if lst[i] + lst[i+1] < lst[i+1] + lst[i]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]

                    flag_sort = False

        return lst
        