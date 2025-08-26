### Basic List Operations

# Create a list
my_list = [1, 2, 3, 4, 5]
print(f"Original list: {my_list}")

# Access elements
# Access the third element (lists are zero-indexed)
print(f"Third element: {my_list[2]}")
# Access the last element using negative indexing
print(f"Last element: {my_list[-1]}")

# Modify an element
my_list[1] = 20
print(f"List after modifying the second element: {my_list}")

# Append an element to the end of the list
my_list.append(6)
print(f"List after appending 6: {my_list}")

# Insert an element at a specific index
# Inserts 10 at index 2
my_list.insert(2, 10)
print(f"List after inserting 10 at index 2: {my_list}")

# Remove an element by value
# Removes the first occurrence of 20
my_list.remove(20)
print(f"List after removing 20: {my_list}")

# Pop an element (removes and returns an element from a specific index)
popped_element = my_list.pop(0)
print(f"Popped element from index 0: {popped_element}")
print(f"List after popping the element: {my_list}")

# Delete an element by index
del my_list[2]
print(f"List after deleting the element at index 2: {my_list}")

# Find the index of a value
index_of_6 = my_list.index(6)
print(f"Index of 6: {index_of_6}")

# Clear the list
my_list.clear()
print(f"List after clearing: {my_list}")
