class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        start = 0
        end = N - 1

        if(N == 1):
            if(nums[0] == target):
                return 0
            else:
                return - 1

        min_index = 0
        
        while(start <= end):
            if nums[start] < nums[end]:
                min_index = start
                break
            mid = (start + end) // 2
            prev_index = (mid + N - 1) % N
            next_index = (mid + 1) % N

            if(nums[mid] < nums[prev_index] and nums[mid] < nums[next_index]):
                min_index = mid
                break
            elif(nums[start] <= nums[mid]):
                start = mid + 1
            elif(nums[mid] <= nums[end]):
                end = mid - 1
            else:
                continue
        
        start = 0
        pivot1 = min_index - 1
        pivot2 = min_index
        end = N - 1

        print(min_index)

        target_index = -1

        while(start <= pivot1):
            mid = (start + pivot1) // 2
            if(nums[mid] == target):
                target_index = mid
                break
            elif(nums[mid] < target):
                start = mid + 1
            else:
                pivot1 = mid - 1
        
        if(target_index == -1):
            while(pivot2 <= end):
                mid = (pivot2 + end) // 2
                if(nums[mid] == target):
                    target_index = mid
                    break
                elif(nums[mid] <  target):
                    pivot2 = mid + 1
                else:
                    end = mid - 1
    
        return target_index
