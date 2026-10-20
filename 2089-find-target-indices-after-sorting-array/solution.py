// 1 ms | 19.2 MB
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        targetlist = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                targetlist.append(i)
        return targetlist