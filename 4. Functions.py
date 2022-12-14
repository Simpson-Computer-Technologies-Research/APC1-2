
# ////////////////////////
# //     Functions      //
# ////////////////////////


# //
# // You can pass anything into a function.
# // This includes: strings, functions, ints, floats, etc.
# //

def main():
    # // Basic function call
    print_string()

    # // Call the returned string functions
    returned_string_1 = return_string_1()
    returned_string_2: str = return_string_2()

    # // Print the returned strings
    print(
        f"{returned_string_1} acts the same as {returned_string_2}"
    )

    # // Passing a variable to a function
    print_passed_variable("a passed string 1")
    print(
        return_passed_variable("a passed string 2")
    )

    # // Optional Parameters
    optional_params(1, string = "optional string")


# ///////////////////////
# //  Basic functions  //
# ///////////////////////
def print_string():
    print("a printed string")

def return_string_1():
    return "returned string 1"

def print_passed_variable(string):
    print(string)


# ////////////////////////
# // Advanced functions //
# ////////////////////////
def return_string_2() -> str:
    return "returned string 2"

def return_passed_variable(string: str) -> str:
    return string


# // The '_' stands for an empty parameter and
# // the string parameter is optional
# //
# // The '_' variable is also seen in lesson 5: loops
def optional_params(_, string = None):
    if string is not None:
        print(string)
    else:
        print("No string provided")


# // If the current script you are running
# // is the main script, call the main function.
# //
# // This is used to prevent custom imports from running
# // unwanted functions.
if __name__ == "__main__":
    main()
