// 46 ms | 19.2 MB
class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        y = abs(x)
        if x == 0:
            return 0
        if x > 0:
            while x>0:
                reverse = reverse*10 + x%10
                x//=10
            if reverse < 2**31-1:
                return reverse
            return 0 
        if x<0:
            while y>0:
                reverse = reverse*10 + y%10
                y//=10
            if reverse < 2**31:
                return -reverse
            return 0 
            