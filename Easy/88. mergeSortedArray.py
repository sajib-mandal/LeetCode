class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Last index nums1
        k = m + n - 1
        # Last index nums1 without non-zero elements
        i = m - 1
        # Last index num2
        j = n - 1

        # Marge nums1 and nums2 in non-decreassing order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        # If nums2 has remaining elemets, copy them all to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
