// 51 ms | 51.4 MB
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge_hash = {}
        for i in knowledge:
            knowledge_hash[i[0]] = i[1]
        string = ''
        i = 0
        while i < len(s):
            if s[i] == '(':
                j = i+1
                key = ''
                while s[j] != ')':
                    key+=s[j]
                    j+=1
                if key in knowledge_hash:
                    string+=knowledge_hash[key]
                else:
                    string+='?'
                i = j+1
            else:
                string +=s[i]
                i+=1
        return string



        