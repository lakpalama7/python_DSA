class Node:
    def __init__(self, data):
        self.prev=None
        self.data=data
        self.next=None

    def forwardTraverse(head):
        firstNode=head
        currentnode=head

        while currentnode:
            print(currentnode.data, end="->")
            if currentnode.next == firstNode:
                break
            currentnode=currentnode.next
        print('null')

    def backwardTraverse(tail):
        lastNode=tail
        currentNode=tail

        while currentNode:
            print(currentNode.data, end='->')
            if currentNode.prev == lastNode:
                break
            currentNode = currentNode.prev
        print('null')


n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)

n1.prev=n5
n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3
n4.next=n5
n5.prev=n4
n5.next=n1

print("Moving forward: ")
Node.forwardTraverse(n1)
print("Backward traveling:")
Node.backwardTraverse(n5)