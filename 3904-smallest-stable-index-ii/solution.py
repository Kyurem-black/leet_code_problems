// 154 ms | 32.3 MB
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maximum = float("-inf")
        minimum = float("inf")
        z = []

        for i in range(len(nums) - 1, -1, -1):
            minimum = min(nums[i], minimum)
            z.append(minimum)
        z.reverse()

        for i in range(len(nums)):
            maximum = max(maximum, nums[i])  
            if maximum - z[i] <= k:
                return i

        return -1