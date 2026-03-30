class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        half = length // 2

        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        
        left, right = 0, len(A) - 1

        while True:
            i = (left + right) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if length % 2:
                    return min(Bright, Aright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            if Aleft > Bright:
                right = i - 1
            elif Bleft > Aright:
                left = i + 1