class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums_length = len(nums)

        sorted_nums = sorted(nums)

        for i in range(nums_length):
            low = i + 1
            high = nums_length - 1
            if(sorted_nums[i] > 0):
                break
            if(i > 0 and sorted_nums[i] == sorted_nums[i-1]):
                continue
            while(low < high):
                three_sum = sorted_nums[i] + sorted_nums[low] + sorted_nums[high]
                if(three_sum == 0):
                    result.append([sorted_nums[i], sorted_nums[low], sorted_nums[high]])
                    low = low + 1
                    high = high - 1
                    while(low < high and sorted_nums[low] == sorted_nums[low - 1]):
                        low = low + 1
                elif(three_sum < 0):
                    low = low + 1
                else:
                    high = high - 1
                
        
        return result

