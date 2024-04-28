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
sol = Solution()
nums = [2, 7, 11, 15]
target = 18
result = sol.twoSum(nums, target)
print("Indices of the two numbers:", result)
