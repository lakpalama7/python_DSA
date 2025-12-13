my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n=len(my_array)

for i in range(1,n):
    current_index=i
    for j in range(i-1,-1,-1): 
        if  my_array[j] > my_array[current_index]: 
            my_array[j], my_array[current_index] = my_array[current_index], my_array[j] 
            current_index=current_index-1

print(my_array)

print("**"*10)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1,n):
    insert_index = i
    current_value = my_array.pop(i)
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            insert_index = j
    my_array.insert(insert_index, current_value)
print(my_array)
     

