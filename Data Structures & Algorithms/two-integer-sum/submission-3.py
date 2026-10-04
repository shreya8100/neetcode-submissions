class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNumMap = {}
        result = [0, 0]

        for index, number in enumerate(nums):
            difference = target - number
            if difference in prevNumMap:
                result = [prevNumMap[difference], index]
                break
            prevNumMap[number] = index
        
        return result
