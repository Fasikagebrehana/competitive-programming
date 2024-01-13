class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        count = {}
        cons_cards = -1
        min_cons_cards = float('inf')
        
        for right in range(len(cards)):
            if cards[right] in count:
                min_cons_cards = min(min_cons_cards, right - count[cards[right]] + 1)
            count[cards[right]] = right
        return min_cons_cards if min_cons_cards != inf else -1