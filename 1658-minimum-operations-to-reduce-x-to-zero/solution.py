// 95 ms | 30.7 MB
class Solution:
    def minOperations(self, nums: list[int], target: int) -> int:
        left = 0
        curr_sum = 0
        total = sum(nums)
        max_len = -1

        if total < target:
            return -1

        for right in range(len(nums)):
            curr_sum+=nums[right]

            while curr_sum > total - target:
                curr_sum -= nums[left]
                left+=1

            if curr_sum == total - target:
                max_len = max(max_len,right - left + 1)

        return -1 if max_len == -1 else len(nums) - max_len
