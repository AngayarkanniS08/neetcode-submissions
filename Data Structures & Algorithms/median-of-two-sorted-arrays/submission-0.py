class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total_size = len(nums1) + len(nums2)
        left_half = total_size // 2
        
        if len(nums1) > len(nums2):
            nums2, nums1 = nums1 , nums2

        left = 0
        right = len(nums1) 
      

        while left <= right:
            mid = (left+right) // 2 

            nums2_left = left_half - mid

            if mid == 0:
                left_1 = float("-inf")
            else:
                left_1 = nums1[mid - 1]

            if mid == len(nums1):
                right_1 = float("inf")
            else:
                right_1 = nums1[mid]

            if nums2_left == 0:
                left_2 = float("-inf")
            else:
                left_2 = nums2[nums2_left - 1]

            if nums2_left == len(nums2):
                right_2 = float("inf")
            else:
                right_2 = nums2[nums2_left]

            if left_1 <= right_2 and left_2 <= right_1:
                if total_size % 2 == 0:
                    left_max = max(left_1, left_2)
                    right_min = min(right_1, right_2)

                    return (left_max + right_min) / 2 

                else:
                    return min(right_1, right_2)

            elif left_1 > right_2:
                right = mid - 1

            else:
                left = mid + 1
        
                






    

        






            

           








