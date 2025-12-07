
queue=[]
queue.append('A')
queue.append('B')
queue.append('C')
print(queue)

print("peek items")
peekitem=queue[0]
print("Front elemenet :", peekitem)

dequeue=queue.pop(0)
print("Deque items: ", dequeue)

print("queue list: ", queue)
print("length of queue: ", len(queue))

print("IS queue empty: ", not bool(queue))