class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0
        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1
        if white_count == 0:
            return 0
        min_op = white_count
        left = 0
        for right in range(k, len(blocks)):
            if blocks[right] == 'W':
                white_count += 1
            if blocks[left] == 'W':
                white_count -= 1
            left += 1
            
            if white_count == 0:
                return 0
            
            min_op = min(min_op, white_count)
            
            
        return min_op
            