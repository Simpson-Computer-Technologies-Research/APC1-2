
# //////////////////////////
# //      Statements      //
# //////////////////////////

# // Declare a variable
my_name: str = "Tristan"

# // Utilize statements to determine
# // what to print to the screen
if my_name == "tristan":
    print("name is in lowercase")

elif my_name == "daniel":
    print("my name is my middle name")

else:
    print("my name is unknown")


# // Utilizing booleans
my_name_is_tristan: bool = my_name == "Tristan"

# // Utilize the if statements
if my_name_is_tristan == True:
    print("True")

elif my_name_is_tristan != True:
    print("False")


# // A better, cleaner, faster and easier way
# // to declare the statement above is as so
if my_name_is_tristan:
    print("True")

elif not my_name_is_tristan:
    print("False")



# ////////////////////
# //  'in' keyword  //
# ////////////////////

# // Check if substring exists in a string
if 'a' in "Tristan":
    print("found 'a' in string")

if 'a' not in "Tristan":
    print("can't find 'a' in string")


# // Check if value is in a list
my_list: list[str] = ['a', 'b', 'c']
if 'a' in my_list:
    print("found 'a' in my_list")

if 'a' not in my_list:
    print("can't find 'a' in my_list")


# // Check if key is in a dictionary
my_dict: dict[str, int] = {
    "age": 16,
    "time": 10
}
if "time" in my_dict:
    print("found time")
elif "time" not in my_dict:
    print("can't find time")
