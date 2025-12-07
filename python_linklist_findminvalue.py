class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

    def findMinValue(head):
        minvalue=head.data
        currentNode=head.next
        while currentNode:
            if currentNode.data < minvalue:
                minvalue=currentNode.data
            currentNode=currentNode.next
        return minvalue
                

n1=Node(5)
n2=Node(10)
n3=Node(0)
n4=Node(50)
n5=Node(2)
n6=Node(1)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6

print("The lowest value in the linklist is :", Node.findMinValue(n1))