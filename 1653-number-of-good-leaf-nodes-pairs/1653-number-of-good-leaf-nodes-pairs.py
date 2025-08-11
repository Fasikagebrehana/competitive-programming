# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        # first collect the leaf nodes 
        # then create a bidirectional graph and do a bfs level order traversal
        # multisource bfs

        graph = defaultdict(list)
        leafs = set()
        def helper(root):
            if not root:
                return
            if not root.left and not root.right:
                # queue.append((root.val, 0))
                leafs.add(root)
            if root.left:
                graph[root].append(root.left)
                graph[root.left].append(root)
            if root.right:
                graph[root].append(root.right)
                graph[root.right].append(root)

            helper(root.left)
            helper(root.right)
            # return 
        helper(root)
        count = 0
        # print(queue)
        # print(graph[root.val])
        def bfs(source):
            nonlocal count
            queue = deque()
            visited = set({source})
            queue.append((source, 0))

            while queue:
                node, dis = queue.popleft()
                if node != source and dis <= distance and node in leafs:
                    count += 1
                visited.add(node)

                for neigh in graph[node]:
                    if neigh not in visited:
                        queue.append((neigh, dis + 1))
                        

        visit = set()
        for leaf in leafs:
            if leaf not in visit:
                visit.add(leaf)
                bfs(leaf)
        # print(count)
        return count // 2