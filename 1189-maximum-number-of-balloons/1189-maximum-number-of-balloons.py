class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {'b': 0, 'a':0, 'l':0, 'o':0, 'n':0}
        for ch in text:
            if ch in freq:
                freq[ch] += 1
        minn = inf
        for key, val in freq.items():
            if key == 'o' or key == 'l':
                minn = min( minn, val//2)
            else:
                minn = min(minn, val)
        return minn