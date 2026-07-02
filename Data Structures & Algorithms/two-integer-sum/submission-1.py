class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        nums_length = len(nums)

        for i in range(nums_length):
            num1 = nums[i]
            for j in range(i+1, nums_length):
                num2 = nums[j]
                if(num1 + num2 == target and  i!=j):
                    result = [i, j]
                    return result
