class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        mid = total // 2
        
        p1 = p2 = 0
        prev = curr = 0
        
        for _ in range(mid + 1):
            prev = curr
            if p1 < m and (p2 >= n or nums1[p1] <= nums2[p2]):
                curr = nums1[p1]
                p1 += 1
            else:
                curr = nums2[p2]
                p2 += 1
                
        if total % 2 != 0:
            return float(curr)
        return (prev + curr) / 2.0
        