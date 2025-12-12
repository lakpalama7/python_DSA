list_value=[7, 3, 9, 12, 11]

n=len(list_value)

for i in range(n):
    swapped=False
    for j in range(n-1-i):
        if list_value[j] > list_value[j+1]:
            list_value[j], list_value[j+1] = list_value[j+1] , list_value[j]
            swapped=True
    if not swapped:
        break

print(list_value)

        

