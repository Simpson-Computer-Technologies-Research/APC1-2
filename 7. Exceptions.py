
# //////////////////
# //  Exceptions  //
# //////////////////

# // There are many different types of exceptions
# // For example there are Division Errors, Value Errors, etc.


# // Catch all errors and ignore them
try:
    print(0/0)
except Exception:
    pass


# // Catch all errors and print the error
try:
    print(0/0)
except Exception as e:
    print(e)


# // Catch only a division by zero error
try:
    print(0/0)
except ZeroDivisionError:
    exit("cannot divide by zero")
