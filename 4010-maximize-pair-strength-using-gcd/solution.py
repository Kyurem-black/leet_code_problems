// 4324 ms | 19.4 MB
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        maximum = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                maximum = max(maximum,(nums[i] * nums[j]) / gcd(nums[i], nums[j])**2)
        return int(maximum)

        