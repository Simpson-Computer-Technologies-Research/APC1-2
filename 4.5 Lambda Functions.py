
# ///////////////////////////////
# //     Lambda Functions      //
# ///////////////////////////////

# //
# // Lambda Functions look a bit more complicated
# // than they actually are.
# //

# // Print the variable x
my_lambda_function = lambda x: print(x)

# // Now in my main program, I can call the function
my_lambda_function("lambda: the variable 'x'")

# // Output:
# // >> the variable 'x'


# // The above lambda function is the same as:
def my_normal_function(x):
    print(x)

my_normal_function("normal: the variable 'x'")