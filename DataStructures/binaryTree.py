class Node:
   def __init__(self, val):
      self.left = None
      self.right = None
      self.val = val
class Tools:
   #BFS(Breadth First Search)
   @staticmethod
   def levelOrder(root):
        levels = []
        if not root:
            return levels
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])
            # append the current node value
            levels[level].append(node.val)
            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
        helper(root, 0)
        return levels
if __name__ == '__main__':
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    print(Tools.levelOrder(root))