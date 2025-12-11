
data_list = [[] for _ in range(10)]

def hashfunction(value):
    sum_char_count=0
    for char in value:
        sum_char_count+=ord(char)
    return sum_char_count%10

def add(value):
    index=hashfunction(value)
    if value is data_list[index]:
        data_list[index].append(value)
    else:
        data_list[index].append(value)

def contains(value):
    index=hashfunction(value)
    if value in data_list[index]:
        return data_list[index]

add("raju")
add("hari")
add('Lisa')
add('Siri')
add('Stuart')
add('hari')
add("amit")

print(data_list)
print("the name is in the list: ", contains("Stuart"))
print(data_list[3])
