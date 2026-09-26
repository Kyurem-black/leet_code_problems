// 37 ms | 30.7 MB
class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        chemistry = 0
        left = 0
        right = len(skill)-1
        prev = skill[left] + skill[right]
        while left < right:
            value = skill[left] + skill[right]
            chemistry += skill[left] * skill[right]
            if value != prev:
                return -1
                break
            left+=1
            right-=1
        return chemistry
            

