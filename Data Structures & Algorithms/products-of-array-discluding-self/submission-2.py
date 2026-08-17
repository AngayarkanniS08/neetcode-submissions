class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        zero_count = 0
        total_product = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product = num * total_product
        for num in nums:
            if zero_count > 1:
                products.append(0*len(nums))
                
            elif zero_count == 1:
                if num == 0:
                    products.append(total_product)
                else:
                    products.append(0)
            else:
                products.append(total_product//num)
        return products