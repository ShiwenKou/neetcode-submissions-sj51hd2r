class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        length = len(A) + len(B)

        half = length // 2
        # we do binary search on A, to find the right partition.
        left, right = 0, len(A) - 1
        while True: # we are not dealing with paris, so use <=

            i = (left + right) // 2
            j = half - i-2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if i + 1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if length % 2: # odd
                    return min(Aright, Bright)
                else:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
            if Aleft > Bright: # move to left portion
                right = i - 1
            else:
                left = i + 1

        