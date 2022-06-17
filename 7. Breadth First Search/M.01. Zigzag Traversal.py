from collections import deque
from logging import RootLogger


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    
    if not root:
        return None

    queue = deque()
    queue.append(root)
    level = -1
    i = 0

    while queue:
        levelResult = deque()
        levelSize = len(queue)

        for _ in range(levelSize):
            node = queue.popleft()

            if level ** i > 0:
                levelResult.append(node.val)
            else:
                levelResult.appendleft(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(list(levelResult))

        i += 1

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
