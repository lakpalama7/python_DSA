
class Queue:
    def __init__(self):
        self.queue=[]

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            print("Queue is empty")

        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(50)
print("queue values are: ", q.queue)

print("Dequeue value is : ", q.dequeue())
print("Queue list are : ", q.queue)
print("Queue size is :", q.size())
print("Queue peek value is : ", q.peek())
print("Queue values are : ", q.queue)
q.enqueue(100)
q.enqueue('a')
print("Queue final values are : ", q.queue)
q.dequeue()
q.dequeue()
print("Final list are : ", q.queue)