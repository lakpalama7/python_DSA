class Node:
    def __init__(self, data):
        self.prev=None
        self.data=data
        self.next=None

    def forwardTraverse(head):
        currentnode=head
        while currentnode:
            print(currentnode.data, end="->")
            currentnode=currentnode.next
        print("null")

    def backwardTraverse(tail):
        currentnode=tail
        while currentnode:
            print(currentnode.data, end="->")
            currentnode=currentnode.prev
        print("null")

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)


n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3
n4.next=n5
n5.prev=n4
n5.next=None

print("Forward traveling:")
Node.forwardTraverse(n1)
print("Backward Traveling: ")
Node.backwardTraverse(n5)
