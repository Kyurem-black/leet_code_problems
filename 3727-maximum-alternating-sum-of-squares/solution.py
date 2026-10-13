// 142 ms | 32.7 MB
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        result = []
        mid = len(nums)//2
        for i in nums:
            result.append(i*i)
        result.sort()
        negative = sum(result[:mid])
        positive = sum(result[mid:])
        return positive - negative
        