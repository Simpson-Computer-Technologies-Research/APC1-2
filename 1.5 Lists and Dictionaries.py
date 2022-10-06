

# /////////////////
# //    Lists    //
# /////////////////
list_1 = ["hey", 0, 1.0]

list_2: list[any] = ["hey", 0, 1.0]

list_3: list[int] = [1, 2, 3]

# // Accessing Lists
list_1_value = list_1[0]
list_2_value = list_1[1]
list_3_value = list_1[2]

# // Setting specific index in a list
list_1[1] = "new item"

# // Adding an item to a list
list_1.append("new item")

# // Removing an item from a list
del list_1[0]

# // Finding index of item
item_at_index: int = list_2.index(0) # // 1

# // Get length of a list
list_1_length: int = len(list_1)


# ////////////////////////
# //    Dictionaries    //
# ////////////////////////
dictionary_1 = {
    "name": "tristan",
    "age": 16
}
dictionary_2: dict[str, str] = {
    "name": "tristan",
    "age": "16"
}

# // Accessing Dictionaries
dictionary_1_name = dictionary_1["name"]
dictionary_2_age = dictionary_2["age"]

# // Setting key in dictionary
dictionary_1["name"] = "daniel"
dictionary_2["birthday"] = "october 31st"

# // Delete a key from a dictionary
del dictionary_2["name"]

# // Get length of a dictionary
dictionary_1_length: int = len(dictionary_1)
