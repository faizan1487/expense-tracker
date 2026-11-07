class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Builds:        0
#              /   \
#             2     4
#            /     / \
#           1     3   -1
#          / \     \    \
#         5   1     6    8
root = TreeNode(0)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(1)
root.right.left = TreeNode(3)
root.right.right = TreeNode(-1)
root.left.left.left = TreeNode(5)
root.left.left.right = TreeNode(1)
root.right.left.right = TreeNode(6)
root.right.right.right = TreeNode(8)

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        # start a queue with the root
        # 

        from collections import deque

        queue = deque()

        queue.append(root)
        levels = []
        while queue:
            length = len(queue)
            level = []
            while length > 0:
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                length -= 1
            if level:
                levels.append(level)

        return levels


sol = Solution()
print(sol.levelOrder(root))
