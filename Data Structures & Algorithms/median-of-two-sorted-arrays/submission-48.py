class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        length = len(A) + len(B)

        if len(A) > len(B):
            A, B = B, A
        
        half = length // 2

        left, right = 0, len(A) - 1

        while True:
            i = (left + right) // 2
            j = half - i - 2
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')


            if Aleft <= Bright and Bleft <= Aright: # partion is correct

                if length % 2:
                    return min(Aright, Bright)
                else:
                    return (min(Aright, Bright) + max(Bleft, Aleft)) / 2

            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1