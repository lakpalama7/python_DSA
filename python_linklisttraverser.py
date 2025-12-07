

class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

    
    def traverseAndPrint(head):
        currentNode=head
        while currentNode:
            print(currentNode.value, end="->")
            currentNode=currentNode.next
        print("done")

n1=Node(5)
n2=Node(10)
n3=Node(40)
n4=Node(50)

n1.next=n2
n2.next=n3
n3.next=n4

Node.traverseAndPrint(n1)


        