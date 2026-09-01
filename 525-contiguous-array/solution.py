// 75 ms | 25.2 MB
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maximum = 0
        x = 0
        first_seen = {0:-1}
        for  i in range(len(nums)):
            if nums[i] == 1:
                x+=1
            else:
                x-=1
            if x in first_seen:
                maximum = max(maximum,i-first_seen[x])
            else:
                first_seen[x] = i
        return maximum
            
