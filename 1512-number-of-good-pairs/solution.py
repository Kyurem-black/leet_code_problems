// 0 ms | 19.2 MB
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x = 0
        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] = 1
        for i in freq:
            x += freq[i] * (freq[i] -1) // 2
        return x



        