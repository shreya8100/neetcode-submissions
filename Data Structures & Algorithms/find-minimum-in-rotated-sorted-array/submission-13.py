class Solution:
    def findMin(self, nums: List[int]) -> int:
         N = len(nums)

         if(N == 1):
            return nums[0]

         if(N == 2):
            return min(nums[0], nums[1])

         start = 0
         end = N - 1

         min_element = 0


         while(start <= end):
            if(nums[start] < nums[end]):
                min_element = nums[start]
                break
            mid = (start + end)//2
            prev_index = (mid + N - 1)%N
            next_index = (mid + 1)%N

            if(nums[mid] < nums[prev_index] and nums[mid] < nums[next_index]):
                min_element = nums[mid]
                break
            elif(nums[start] <= nums[mid]):
                start = mid + 1
            elif(nums[mid] <= nums[end]):
                end = mid - 1
         return min_element