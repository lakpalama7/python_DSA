stack=[]
stack.append('A')
stack.append('B')
stack.append(1)
print("items in stack:", stack)
print("size of stack:", len(stack)) #return the size of stack, no of items

ritem=stack.pop()
print("Remove item :", ritem)
print("items in stack after pop: ", stack)

itempeek=stack[-1]
print("Peek item: ", itempeek)

isEmpty=not bool(stack)
print("not empty", isEmpty) # stack is not empty
print(bool(stack)) #stack is not empty
print(stack) #print stack value
stack.pop() #remove last value
stack.pop()#remove last value
print(stack) #print value ---its empty now
print(not bool(stack)) #stak is empty, its true