
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(f"My list: {my_list}")

# Insert the value 15 at the second position in the list.
my_list.insert(1,15)
print(f"List after inserting 15 in index 1: {my_list}")

# Extend my_list with another list: [50, 60, 70].
another_list = [50, 60, 70]

my_list.extend(another_list)

print(f"The extended list: {my_list}")

# Remove the last element from my_list.
list_length = len(my_list)
last_element_index = list_length - 1

my_list.pop(last_element_index)

print(f"My list after removing the last item: {my_list}")

# Sort my_list in ascending order.
my_list.sort()

print(f"List in asceding order: {my_list}")

# Find and print the index of the value 30 in my_list.

for items in my_list:
  if items == 30:
    index = my_list.index(items)
    print(f"Index for the value of 30 is {index}.")


