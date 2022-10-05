#first we create a node class with datavalue=None in init and nextvalue=None
class Node:
    def __init__(self,dataValue=None):
        self.dataValue=dataValue
        self.nextValue=None
#next we create a linkedList class with a headValue=None
class LinkedList:
    def __init__(self):
        self.headValue=None
    def printIt(self):
        printValue=self.headValue
        while printValue is not None:
            print(printValue.dataValue)
            printValue=printValue.nextValue

linkedList1=LinkedList()
#create the first node or the head node
linkedList1.headValue=Node("Sun")
#create the second node and link the first node to the second one
n2=Node("Mon")
linkedList1.headValue.nextValue=n2
#create the third node and link the second node to the third one
n3=Node("Tues")
n2.nextValue=n3
linkedList1.printIt()