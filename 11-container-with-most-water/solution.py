// 39 ms | 29.7 MB
class Solution:
    def maxArea(self, height: List[int]) -> int:
        st1 = 0
        n = len(height)
        st2 = n-1
        max = 0

        for i in range(0,n):
            area = 0
            if height[st1] < height[st2]:
                area = (height[st1]) * (st2-st1)
                st1 = st1 + 1
            elif height[st1] > height[st2]:
                area = (height[st2]) * (st2-st1)
                st2 -= 1
            else:
                area = height[st1] * (st2-st1)
                st1 += 1
            if area > max:
                max = area
        
        return max