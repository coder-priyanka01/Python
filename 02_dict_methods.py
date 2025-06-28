marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    0: "priyanka",
}

#print(marks.items())  # returns a view object that displays a list of a dictionary's key-value tuple pairs

#print(marks.keys())  # returns a view object that displays a list of all the keys in the dictionary
#print(marks.values())  # returns a view object that displays a list of all the values in the dictionary

#marks.update({"priyanka": 100, "renuka": 78})  # adds a new key-value pair to the dictionary
#print(marks)

print(marks.get("priyanka"))  # returns the value for the specified key if it exists in the dictionary, otherwise returns None
print(marks["priyanka2"])  # returns the value for the specified key if it exists in the dictionary, otherwise raises a KeyError