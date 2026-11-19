class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]* len(nums)
        prefix = 1
        suffix = 1

        for index, num in enumerate(nums):
            output[index] = prefix
            prefix = prefix * num
            
        for index in range(len(nums)-1, -1, -1):
            output[index] *= suffix
            suffix*= nums[index]

        return output

            





