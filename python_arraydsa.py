my_array = [7, 12, 9, 4, 11]

#find the smallest element

smallest_value=my_array[0]

for value in my_array:
    if value < smallest_value:
        smallest_value=value
print("the smallest value is : ", smallest_value)