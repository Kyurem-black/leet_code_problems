// 0 ms | 19.2 MB
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sumofsquares = 0
        n = len(nums)
        for i in range(n):
            if n % (i+1) == 0:
                sumofsquares += (nums[i]*nums[i])
        return sumofsquares
        