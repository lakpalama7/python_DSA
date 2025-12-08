
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

    def traverseNode(head):
        currentNode=head
        while currentNode:
            print(currentNode.data, end="->")
            currentNode=currentNode.next
        print("null")

    def insertNewNode(head, newNode, position):
        if position==1:
            newNode.next=head
            return newNode
        
        currentNode=head
        preNode=None
        for _ in range(position-1):
            if currentNode is None:
                break
            preNode=currentNode
            currentNode=preNode.next

        newNode.next=currentNode
        preNode.next=newnode

        return head


        
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

print("before adding new node")
Node.traverseNode(n1)

newnode=Node(100)
finalnode=Node.insertNewNode(n1, newnode,7)
print("After adding new node")
Node.traverseNode(finalnode)
