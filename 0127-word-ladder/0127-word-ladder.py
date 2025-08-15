class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # bfs by checking if they difer by one letter by changing each letter transformation and check if its in wordList or not for the lookup we will make the wordList a  set


        letters = "abcdefghijklmnopqrstuvwxyz"
        wordList = set(wordList)

        if endWord not in wordList:
            return 0
        visited = set()
        visited.add(beginWord)
        queue = deque([(beginWord, 1)])
        answer = 0
        while queue:
            node, level = queue.popleft()
            if node == endWord:
                return level

            for i in range(len(node)):
                for ch in letters:
                    newWord = node[:i] + ch + node[i+1:]
                    if newWord in wordList and newWord not in visited:
                        queue.append((newWord, level+1))
                        visited.add(newWord)
        
        return 0