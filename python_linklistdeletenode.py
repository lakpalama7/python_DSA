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

    def deleteNode(head, deletenode):
        if head == deletenode:
            return head.next
        currentNode=head
        while currentNode.next and currentNode.next !=deletenode:
            currentNode=currentNode.next
        if currentNode.next is None:
            return head
        currentNode.next=currentNode.next.next
        deletenode.next=None
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
n5.next=None

print("before deleting")
Node.traverseNode(n1)

deletenode=Node.deleteNode(n1,n4)
print("After deleting: ")
Node.traverseNode(deletenode)