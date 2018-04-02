class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        max_len = max(len1, len2)
        mid_len = (len1 + len2) // 2
        mid_odd = (len1 + len2) % 2

        count = 0
        prev = 0
        
        while (True):
            if count >= mid_len:
                break;
            if not nums1:
                prev = nums2.pop(0)
            elif not nums2:
                prev = nums1.pop(0)
            elif nums1[0] > nums2[0]:
                prev = nums2.pop(0)
            elif nums1[0] < nums2[0]:
                prev = nums1.pop(0)
            else:
                prev = nums1.pop(0)
            count = count + 1

        if not nums1:
            return nums2[0] if mid_odd > 0 else (nums2[0]+prev)/2.0
        elif not nums2:
            return nums1[0] if mid_odd > 0 else (nums1[0]+prev)/2.0
        elif nums1[0] < nums2[0]:
            return nums1[0] if mid_odd > 0 else (nums1[0]+prev)/2.0
        elif nums1[0] > nums2[0]:
            return nums2[0] if mid_odd > 0 else (nums2[0]+prev)/2.0
        else:
            return nums1[0] if mid_odd > 0 else (nums1[0]+prev)/2.0
        
#---------------------------
a = Solution()
print a.findMedianSortedArrays([1, 3], [2])
print a.findMedianSortedArrays([1, 2], [3, 4])
print a.findMedianSortedArrays([1, 2], [1, 2])
