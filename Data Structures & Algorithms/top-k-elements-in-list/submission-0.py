class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_nums = Counter(nums)
        
        maximum_freq = 0
        maximum_num = 0

        most_common = frequency_nums.most_common()
        result = []

        for i in range(0, k):
            result.append(most_common[i][0])

        return result