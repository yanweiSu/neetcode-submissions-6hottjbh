class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        
        n = len(nums1)
        m = len(nums2)
        half = (n + m) // 2
        i = n // 2
        j = half - i

        while (i > 0 and i < n):
            if nums1[i-1] > nums2[j]:
                i -= 1
                j = half - i
            elif nums2[j-1] > nums1[i]:
                j -= 1
                i = half - j
            else:
                break

        l1, l2, r1, r2 = -float("inf"), -float("inf"), float("inf"), float("inf")
        if i > 0:
            l1 = nums1[i-1]
        if j > 0:
            l2 = nums2[j-1]
        if i < n:
            r1 = nums1[i]
        if j < m:
            r2 = nums2[j]

        if (n + m) % 2 == 1:
            return min(r1, r2)
        else:
            return 0.5 * (max(l1, l2) + min(r1, r2))