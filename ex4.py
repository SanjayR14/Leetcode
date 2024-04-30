class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        
        # Find median
        total_length = len(merged)
        if total_length % 2 == 1:
            return merged[total_length // 2]
        else:
            mid_right = total_length // 2
            mid_left = mid_right - 1
            return float(merged[mid_left] + merged[mid_right]) / 2
nums1 = list(map(int, input("Enter the elements of the first sorted array separated by space: ").split()))
nums2 = list(map(int, input("Enter the elements of the second sorted array separated by space: ").split()))
solution = Solution()

median = solution.findMedianSortedArrays(nums1, nums2)
print("Median of the merged sorted arrays:", median)
