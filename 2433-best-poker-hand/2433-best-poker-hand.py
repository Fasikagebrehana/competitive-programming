class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rank_freq = Counter(ranks)
        suits_freq = Counter(suits)
        answer = inf
        for i in range(len(ranks)):
            if suits_freq[suits[i]] >= 5:
                return "Flush"
            elif rank_freq[ranks[i]] >= 3:
                answer = min(answer, 2)
            elif rank_freq[ranks[i]] >= 2:
                answer = min(answer, 3)
            else:
                answer = min(answer, 4)

        if answer == 2:
            return "Three of a Kind"
        elif answer == 3:
            return "Pair"
        else:
            return "High Card"