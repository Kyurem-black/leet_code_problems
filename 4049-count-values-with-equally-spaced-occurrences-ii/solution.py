// 299 ms | 50.2 MB
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq = {}
        for key , value in enumerate(nums):
            if value in freq:
                temp = freq[value]
                if temp[1] == -1:
                    if temp[2] == 1:
                        freq[value] = [key,key-temp[0],temp[2]+1]
                    continue
                if temp[1] != -1 and key-temp[0] != temp[1]:
                    freq[value] = [key,-1,temp[2]+1]
                else:
                    freq[value] = [key, temp[1], temp[2] + 1]
            else:
                freq[value] = [key,-1,1]
        ans = 0
        for i in freq:
            idx = freq[i]
            if idx[1] != -1 and idx[2] >= 3:
                ans+=1
        return ans


        

        
        