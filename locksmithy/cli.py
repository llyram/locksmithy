import locksmith
import argparse
def main():
    parser = argparse.ArgumentParser(description='Generate a random password')
    parser.add_argument('-l', '--length', type=int, default=10,
                        help='the length of the password (default: 10)')
    parser.add_argument('-n', '--no-numbers', action='store_false', dest='include_numbers',
                        help='exclude numbers from the password')
    parser.add_argument('-s', '--no-special-chars', action='store_false', dest='include_special_chars',
                        help='exclude special characters from the password')
    parser.add_argument('-u', '--no-uppercase', action='store_false', dest='include_uppercase_chars',
                        help='exclude uppercase letters from the password')
    parser.add_argument('-a', '--all', action='store_true', default=True,
                        help='include all character types in the password (default: True)')
    args = parser.parse_args()
    try:
        password = locksmith.generate_password(args.length, args.include_numbers, args.include_special_chars, args.include_uppercase_chars, args.all)
        print(password)
    except ValueError as e:
        print(e)
main()