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

if __name__=='__main__':
    tree=NAryTree()
    tree.root=Node(1)
    tree.addChild(2)
    tree.addChild(3)
    tree.child[0].addChild(21)
    tree.child[0].addChild(22)
    tree.child[0].addChild(23)
    tree.child[1].addChild(31)
    tree.child[1].addChild(32)
    tree.child[1].addChild(33)
