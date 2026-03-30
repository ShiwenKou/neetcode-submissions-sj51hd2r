class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1) - 1
        while True:

            mid = (left + right) // 2
            j = half - mid - 2

            nums1Left = nums1[mid] if mid >=0 else float('-inf')
            nums1Right = nums1[mid+1] if mid+1 < len(nums1) else float('inf')
            nums2Left = nums2[j] if j >=0 else float('-inf')
            nums2Right = nums2[j+1] if j+1 < len(nums2) else float('inf')

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if total % 2:
                    return min(nums1Right, nums2Right)
                else:
                    return (max(nums1Left , nums2Left) + min(nums1Right, nums2Right)) / 2
            elif nums1Left > nums2Right:
                right = mid -1
            elif nums2Left > nums1Right:
                left = mid + 1
        