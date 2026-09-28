// 0 ms | 19.2 MB
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maximum = 0
        for i in s:
            if i == '(':
                count+=1
            if i == ')':
                count-=1
            maximum = max(maximum,count)
        return maximum


        