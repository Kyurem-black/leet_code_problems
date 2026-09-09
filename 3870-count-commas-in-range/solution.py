// 0 ms | 19.3 MB
class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        return (n - 1000) +1