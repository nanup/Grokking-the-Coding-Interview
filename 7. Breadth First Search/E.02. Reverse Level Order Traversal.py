from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = deque()

  if not root:
    return result
    
  queue = deque()

  queue.append(root)

  while queue:
    levelResult = []
    levelSize = len(queue)

    for i in range(levelSize):
      node = queue.popleft()
      levelResult.append(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

    result.appendleft(levelResult)

  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()