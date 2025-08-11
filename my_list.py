# Creating the list

my_list = []

for i in range(10, 50, 10):
    my_list.append(i)

# check
print(my_list)

my_list.insert(1, 15)
# check
print(my_list)

extend_list = [50, 60, 70]
my_list.extend(extend_list)
print("extended list")
print(my_list)

my_list.pop(-1)
print("popped last list")
print(my_list)

sorted(my_list)
print("sorted")
print(my_list)

print("find and print index")
print(my_list[3])