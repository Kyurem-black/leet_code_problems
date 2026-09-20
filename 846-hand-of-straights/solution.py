// 31 ms | 21.1 MB
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = {}

        for card in hand:
            freq[card] = freq.get(card, 0) + 1

        hand.sort()

        for card in hand:
            if freq[card] == 0:
                continue

            for i in range(groupSize):
                current = card + i

                if freq.get(current, 0) == 0:
                    return False

                freq[current] -= 1

        return True