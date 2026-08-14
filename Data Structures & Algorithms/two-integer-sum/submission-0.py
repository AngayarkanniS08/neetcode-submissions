class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         target_index= {}

         for index,value in enumerate(nums):
            complement = target - value
            if complement in target_index:
                return [target_index[complement], index]
            target_index[value] = index

            


         