class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_length = len(numbers)
        
        start = 0
        end = nums_length - 1
        result = [0] * 2

        while(start < end):
            if(numbers[start] + numbers[end] == target):
                result = [start + 1, end + 1]
                break
            elif(numbers[start] + numbers[end] > target):
                end = end - 1
            elif(numbers[start] + numbers[end] < target):
                start = start + 1
        
        return result