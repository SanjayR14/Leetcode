# Define the Solution class and the twoSum method
class Solution():
    def twoSum(self,nums, target):
        empty_dict = {}
        n = len(nums)
        for index in range(n):
            some_number = target - nums[index]
            if some_number in empty_dict:
                return [empty_dict[some_number], index]
            empty_dict[nums[index]] = index
            print(index)
        return []

# Create an instance of the Solution class
sol = Solution()

# Define the input list and target sum
nums = [2, 7, 11, 15]
target = 18


# Call the twoSum method with the input
result = sol.twoSum(nums, target)

# Print the result
print("Indices of the two numbers:", result)
