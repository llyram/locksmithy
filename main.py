import random
import string
import argparse
import sys

# create an argument parser
parser = argparse.ArgumentParser(description='Generate a random password.')

# add the length argument
parser.add_argument('-l', '--length', type=int, default=10, help='the length of the password')

# add boolean flags for including numbers, special characters, uppercase letters, and lowercase letters
parser.add_argument('-n', '--numbers', action='store_false', default=True, help='exclude numbers from the password')
parser.add_argument('-s', '--special', action='store_false', default=True, help='exclude special characters from the password')
parser.add_argument('-u', '--uppercase', action='store_false', default=True, help='exclude uppercase letters from the password')
parser.add_argument('-w', '--no-lowercase', dest='lowercase', action='store_false', default=True, help='exclude lowercase letters from the password')

# parse the arguments
args = parser.parse_args()

# define the characters to be used in the password
all_chars = ''
if args.numbers:
    all_chars += string.digits
if args.special:
    all_chars += string.punctuation
if args.uppercase:
    all_chars += string.ascii_uppercase
if args.lowercase:
    all_chars += string.ascii_lowercase

# ensure that at least one character set is included
if not all_chars:
    print('Error: At least one set of characters must be included in the password')
    sys.exit(1)

# generate the password
password = ''.join(random.choices(all_chars, k=args.length))
print(password)
