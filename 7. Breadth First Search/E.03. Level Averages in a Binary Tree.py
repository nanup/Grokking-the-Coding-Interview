from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    queue = deque()
    queue.append(root)

    while queue:
        sum = 0
        levelSize = len(queue)

        for _ in range(levelSize):
            node = queue.popleft()
            sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        avg = sum / levelSize
        result.append(avg)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
