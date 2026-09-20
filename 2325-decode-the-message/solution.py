// 3 ms | 19.3 MB
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        freq = {}
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        idx = 0
        for i in key:
            if i != " " and i not in freq:
                freq[i] = alphabets[idx]
                idx +=1
        sol = ""
        for i in message:
            if i == " ":
                sol+=" "
            else:
                sol+=freq[i]
        return sol
