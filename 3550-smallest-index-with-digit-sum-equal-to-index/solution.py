// 0 ms | 19.4 MB
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            value = 0
            if nums[idx] > 9:
                x = str(nums[idx])
                for i in x:
                    value += int(i)
                if value == idx:
                    return idx
            if nums[idx] < 10 and nums[idx] == idx:
                return idx
            
        return -1
