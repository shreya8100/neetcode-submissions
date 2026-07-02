class Solution:
    def hasDuplicate(self, nums) -> bool:
        nums_set = set()
        for i in range(len(nums)):
            nums_set.add(nums[i])
        result = False
        print(len(nums_set))
        print(len(nums))
        if len(nums_set) == len(nums):
            result = False
        else:
            result = True
        return result

            
        