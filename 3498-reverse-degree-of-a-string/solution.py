// 7 ms | 19.2 MB
class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        idx = 1
        for i in s:
            value = 26 - (ord(i) - ord('a'))
            total += idx * value
            idx+=1
        return total



        