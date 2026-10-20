class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_side_product = []
        current_prod = 1

        for i in nums:
            left_side_product.append(current_prod)
            current_prod = i * current_prod

        print(left_side_product)

        right_side_product = []
        current_prod = 1

        for i in nums[::-1]:
            right_side_product.append(current_prod)
            current_prod = i * current_prod

        result = []
        
        for index, i in enumerate(right_side_product[::-1]):
            result.append(left_side_product[index] * i)


        result result

        

        


sol = Solution()
nums = [1,2,3,4]
print(sol.productExceptSelf(nums))
