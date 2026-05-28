from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2

        left, right = 0, m
        while left <= right:
            partition1 = (left + right) // 2 # cut nums1 at partition1
            partition2 = total_left - partition1 # cut nums2 accordingly

            # Handle edge cases: if partition is 0 or len(arr)
            max_left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            min_right1 = nums1[partition1] if partition1 < m else float('inf')

            max_left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            min_right2 = nums2[partition2] if partition2 < n else float('inf')

            # Check if we found correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Found it
                if (m + n) % 2 == 0: # even total
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else: # odd total
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                # partition1 too big, move left
                right = partition1 - 1
            else:
                # partition1 too small, move right
                left = partition1 + 1