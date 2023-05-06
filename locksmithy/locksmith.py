import random, string
def generate_password(length, include_numbers, include_special_chars, include_uppercase_chars, include_lowercase_chars):
    all_chars = string.ascii_lowercase
    if include_numbers:
        all_chars += string.digits
    if include_special_chars:
        all_chars += string.punctuation
    if include_uppercase_chars:
        all_chars += string.ascii_uppercase
    if all_chars == string.ascii_lowercase:
        raise ValueError("At least one character type must be included in the password")
    password = ''.join(random.choice(all_chars) for i in range(length))
    return password
