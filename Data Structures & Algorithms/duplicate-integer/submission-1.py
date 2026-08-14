class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        # Loop through the indexes of the list (e.g., 0, 1, 2...)
        for i in range(len(nums)):
            num = nums[i]  # Get the number at the current index

            if num in count:
                return True
            else:
                count[num] = 1

        return False
