def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Check if the string is the same when reversed
    return s == s[::-1]

# Input from user
input_string = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome!")
else:
    print(f"'{input_string}' is not a palindrome.")
