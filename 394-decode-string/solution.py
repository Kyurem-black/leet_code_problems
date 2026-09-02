// 0 ms | 19.4 MB
class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        curr = ''
        stack = []
        for  i in s:
            if i.isdigit():
                num = num* 10 + int(i)
            elif i == '[':
                if num == 0:
                    num = 1
                stack.append((curr,num))
                num = 0
                curr = ''
            elif i == ']':
                prev,count = stack.pop()
                curr = prev + curr*count
            else:
                curr+=i
        return curr

        