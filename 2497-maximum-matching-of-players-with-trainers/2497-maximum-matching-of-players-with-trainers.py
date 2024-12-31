class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i = j = 0
        trainers.sort(reverse=True)
        players.sort(reverse=True)
        max_match = 0
        for i in range(len(players)):
            if j < len(trainers) and players[i] <= trainers[j]:
                max_match += 1
                j += 1

        return max_match