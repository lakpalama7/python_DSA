
value_list=[ 7, 12, 9, 11, 3]

n=len(value_list)

for i in range(n):
    for j in range(n-1-i):
        j+=i
        if value_list[i] > value_list[j+1]:
            value_list[i], value_list[j+1] = value_list[j+1], value_list[i]
print(value_list)

print("***"*10)
my_array = [64, 34, 25, 5, 22, 11, 90, 12]
n=len(my_array)

for i in range(n-1):
    for j in range(i+1,n):
        if my_array[i] > my_array[j]:
            my_array[i], my_array[j] = my_array[j], my_array[i]
print(my_array)

print("***"*10)

my_array = [62, 15, 25, 2, 3, 66, 9, 1]
n=len(my_array)

for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if my_array[min_index] > my_array[j]:
            min_index=j

    smallest_value=my_array.pop(min_index)
    my_array.insert(i, smallest_value)

print(my_array)