// 153 ms | 42 MB
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        freq = {}
        z = []
        count = 0
        for key,value in zip(position,speed):
            freq[key] = value
        position.sort(reverse = True)
        for i in range(len(position)):
            time = (target - position[i]) / freq[position[i]]
            z.append(time)
        last_fleet = 0
        for i in z:
            if i > last_fleet:
                count+=1
                last_fleet = i

            # if z[i] <= z[i-1] and i != 0:
            #     continue
            # else:
            #     count+=1
        return count


        