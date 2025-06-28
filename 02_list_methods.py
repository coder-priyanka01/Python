friends = ["Apple", "Banana", 5, 6.7, True, "Alice"]
print(friends) 

friends.append("Cherry") # Add an element to the end of the list
print(friends)

l1 = [1,34,65,23,45,67,89]
#l1.sort() # Sort the list in ascending order
#l1.reverse() # Reverse the list
#l1.insert(2, 100) # Insert 100 at index 2
#print(l1.pop(3)) # Remove and return the last element of the lis
#l1.pop(2) # Remove the element at index 2

value = l1.pop(2) # Remove the element at index 2 and return it
print(value) # Print the removed value
print(l1)
