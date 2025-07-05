# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = deque([root])
        visited = set()
        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    queue.append(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    queue.append(node.right)
        print(graph)
        level = 0
        target = target.val
        queue = deque()
        answer = []
        def bfs(target, queue):
            visited = set()
            nonlocal answer

            while queue:
                node, level =  queue.popleft()

                visited.add(node)
                if level == k:
                    answer.append(node)

                for neigh in graph[node]:
                    if neigh not in visited:
                        queue.append((neigh, level + 1))
        queue = deque([(target, 0)])
        bfs(target, queue)

        # print(answer)
        return answer
