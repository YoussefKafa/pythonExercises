
#the Node class , every node is [data,next]
class Node:
    def __init__(self,data):
        self.value=data
        self.next=None


# the singly linked list class , we need a head which is initially None 
class SinglyLinkedList:
    def __init__(self):
        self.head=None

#print function
    def print(self):
        #if the linked list is empty , then print an empty list
        if self.head is None:
            print([])
        else:
            #if the linked list is not empty , take the first node (the head ) as the current node 
            curr=self.head
            #create a list to print
            list=[]
            # while the current node is not None , append the node value to the list 
            # and make the current node is equal to the next node that the curr.next points to
            while curr is not None:
                list.append(curr.value)
                curr=curr.next
            #print the list
            print(list)
    
# add to the start function , takes the data value of the added node
    def add_start(self,data):
        #create the new node
        newNode=Node(data)
        #the node next pointer will be the linked list head
        newNode.next=self.head
        #and after that , the linked list head will become the node we've just added.
        self.head=newNode

# add to the tail function
    def add_end(self,data):
        #create the new node
        newNode=Node(data)
        #if the linked list is empty 
        if self.head is None:
        #then the head will become the node we've just created
            self.head=newNode
        else:
        #if it is not empty, we start from the head node as the current node
            curr=self.head
        # we go through the linked list node by node, until we reach a node that has None in the next pointer
            while curr.next is not None:
                curr=curr.next
        #we assign our node to the current node next pointer , and now it's connected
            curr.next=newNode

if __name__ == '__main__':
    ll=SinglyLinkedList()
    ll.add_end(1)
    ll.add_end(2)
    ll.add_end(3)
    ll.print()