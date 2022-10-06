
# ///////////////////////
# //       Loops       //
# ///////////////////////

# // For Range Loop 1
# // This will print the numbers 0, 9 on the screen
def for_range_loop_1():
    for i in range(0, 10):
        print(i)

# // For Range Loop 1
# // This will print the provided string on
# // the screen nine times
def for_range_loop_2(string: str):
    for _ in range(0, 10):
        print(string)

# // So what is the '_'?
# // The '_' means that no variable is assigned.
# // Utilizing this variable helps with controlling
# // unused variables which helps with memory usage.


# // For Variable Loop
# // Converts the contents in the loop
# // to variables which can be accessed.
def for_variable_loop(my_list: list[str]):
    for word in my_list:
        print(word)


# // The enumerate function is used to
# // store the current index of the list
# // along with the variable that can be accessed
def enumerate_loop(my_list: list[str]):
    for i, word in enumerate(my_list):
        print(f"{i}: {word}")


# // While loop
# // This will print 'hi' until the program is closed
def while_loop(word: str):
    while True:
        print(word)

        # // Utilize the 'break' keyword
        # // for stopping a loop.
        # //
        # // The 'break' keyword can be used in
        # // any loop. (for, while, enumerate, etc.)
        if word == "stop":
            break
        
        # // The 'break' keyword can be replaced with
        # // the 'return' keyword
        elif word == "stop again":
            return


# // Run the functions if main file
if __name__ == "__main__":
    # // Call the range_loop functions
    for_range_loop_1()
    for_range_loop_2("range loop 2 string")

    # // Call the for_variable_loop function
    my_list: list[str] = ["my", "name", "is", "dave"]
    for_variable_loop(my_list)

    # // Call the enumerate_loop function
    enumerate_loop(my_list)

    # // Call the while_loop function
    while_loop("while loop's word")
