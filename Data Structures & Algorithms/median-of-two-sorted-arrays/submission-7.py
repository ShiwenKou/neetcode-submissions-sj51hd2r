class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)

        half = length // 2

        A = nums1
        B = nums2
        if len(nums1) > len(nums2):
            A, B = B, A
        left, right = 0, len(A) - 1
        while True:
            mid = (left + right) // 2
            j = half - mid - 2

            Aleft = A[mid] if mid >= 0 else float('-inf')
            Aright = A[mid + 1] if mid + 1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if length % 2:
                    return min(Bright, Aright)
                else:
                    return (min(Bright, Aright) + max(Aleft, Bleft)) / 2
            if Aleft > Bright:
                right = mid - 1
            else:
                left = mid + 1


        