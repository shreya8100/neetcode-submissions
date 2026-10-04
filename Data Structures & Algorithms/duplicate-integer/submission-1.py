class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set()
        result = False

        for i in range(len(nums)):
            numsSet.add(nums[i])

        if(len(numsSet) == len(nums)):
            result = False
        else:
            result = True
        
        return result