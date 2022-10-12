class Node :
    def __init__(self, value) :
        self.value=value
        self.child =  []
    def addChild(self, value) :
        n = Node(value)
        self.child.append(n)
class NAryTree :
    def __init__(self) :
        self.root = None
class Tools:
    """
    Given the root of an n-ary tree, return the preorder traversal (dfs) of its nodes' values.
    Input: root = [1,null,3,2,4,null,5,6]
    first node:1 and its children (3,2,4)
    children of 3 are 5,6.
Output: [1,3,5,6,2,4]
    """
    @staticmethod
    def dfs(root:'Node') -> list[int]:
        if root is None:
            return []
        stack,output=[root,],[]
        while stack:
            root=stack.pop()
            output.append(root.value)
            stack.extend(root.child[::-1])
        return output
if __name__=='__main__':
    tree=NAryTree()
    tree.root=Node(1)
    tree.root.addChild(2)
    tree.root.addChild(3)
    tree.root.child[0].addChild(21)
    tree.root.child[0].addChild(22)
    tree.root.child[0].addChild(23)
    tree.root.child[1].addChild(31)
    tree.root.child[1].addChild(32)
    tree.root.child[1].addChild(33)
    print(Tools.dfs(tree.root))

