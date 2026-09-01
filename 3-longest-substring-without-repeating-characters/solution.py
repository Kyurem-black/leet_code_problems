// 205 ms | 19.9 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = set()
        maximum = 0
        left = 0
        for i in range(len(s)):
            while s[i] in x:
                x.remove(s[left])
                left+=1
            x.add(s[i])
                
            maximum = max(maximum,i-left+1)
        return maximum
        