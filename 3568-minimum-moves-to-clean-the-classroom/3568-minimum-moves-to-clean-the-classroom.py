class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        
        start = None
        all_litters = set()
        for i in range(len(classroom)):
            for j in range(len(classroom[0])):
                if classroom[i][j] == "L":
                    all_litters.add((i,j))
                elif classroom[i][j] == 'S':
                    start = (i, j)
        
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        
        queue = deque()
        # row, col, current energy, collected litter, moves
        queue.append((start[0], start[1], energy, frozenset(), 0))
        # frozenset meaning like set but it can't be altered, changed or removed and unlike set it can be used as a key or be inside another set(its hashable)
        visited = {}
        visited[(start[0], start[1], frozenset())] = energy

        while queue:
            r, c, e, collected, moves = queue.popleft()
            if collected == all_litters:
                return moves
            
            for x, y in directions:
                nr, nc = x+r, y+c
                if not (0 <= nr < len(classroom) and 0 <= nc < len(classroom[0])):
                    continue
                # obstacles pass
                if classroom[nr][nc] == 'X':
                    continue
                # if its not out of bound and obstacle it takes energy
                new_energy = e - 1
                if new_energy < 0:
                    continue
                # if its Litter collect it
                new_collected = collected

                if classroom[nr][nc] == "L":
                    # set union operator |
                    new_collected = collected | frozenset([(nr, nc)])
                # if its R recharge
                if classroom[nr][nc] == "R":
                    new_energy = energy
                state = (nr, nc, new_collected)

                if state in visited and visited[state] >= new_energy:
                    continue

                visited[state] = new_energy
                queue.append((nr, nc, new_energy, new_collected, moves + 1))

        return -1


        