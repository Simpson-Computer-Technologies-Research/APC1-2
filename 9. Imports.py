
# /////////////////
# //   Imports   //
# /////////////////

# //
# // You can install libraries using 'pip install {name}'
# // Libraries can be found easily on pypi.org
# //

# // The following libraries are python defaults
import string, sys

# // Import function from a library
from random import choice

# // Import library as a custom name
import datetime as dt


# // Use the string library
letters: str = string.ascii_letters

# // Use the random.choice function
rand_char: str = choice(letters)

# // Use the sys library
if rand_char == 'e':
    sys.exit("Very Unlucky")

# // Use the datetime library
else:
    print(f'The Current Date is: {dt.datetime.now()}')

