class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if(len(nums) == 0):
            return 0

        nums_set = set(nums)
        
        sorted_nums_set = sorted(nums_set)
        
        max_consecutive = 0
        prev_max_consecutive = -1

        print(sorted_nums_set)

        i = 0

        while i<len(sorted_nums_set) - 1:
            if(sorted_nums_set[i] + 1 == sorted_nums_set[i+1]):
                print(max_consecutive, sorted_nums_set[i], sorted_nums_set[i+1])
                max_consecutive += 1
            else:
                if(prev_max_consecutive < max_consecutive):
                    prev_max_consecutive = max_consecutive
                max_consecutive = 0
            i+=1
        
        if(prev_max_consecutive < max_consecutive):
            prev_max_consecutive = max_consecutive
        
        return prev_max_consecutive + 1
                
