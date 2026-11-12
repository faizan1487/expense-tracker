from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

root = build_tree([3, 9, 20, None, None, 15, 7])



class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        from collections import deque
        q = deque()
        q.append(root)
        levels = []
        alternate = True
        while q:
            len_q = len(q)
            level = []
            while len_q > 0:
                node = q.popleft()
                len_q -= 1
                if alternate:
                    if node:
                        level.append(node.val)
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
                    alternate = False
                else:
                    if node:
                        level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    alternate = True
            levels.append(level)

        return levels


sol = Solution()
print(sol.levelOrder(root))
