#metasploit's pattern_ctreate in python for generating buffer overflow sets to test for fault offsets
#Syntax: python3 pattern_create.py <length>
import string, sys

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits

index_digit = 0
index_lower = 0
index_upper = 0

i = 0
while i<=sys.argv[1]:
    current_digit = digits[index_digit % len(digits)]
    current_lower = lowercase_letters[index_lower % len(lowercase_letters)]
    current_upper = uppercase_letters[index_upper % len(uppercase_letters)]

    print(f"{current_upper}{current_lower}{current_digit}", end="")

    index_digit += 1
    if index_digit == len(digits):
        index_digit = 0
        index_lower += 1
    if index_lower == len(lowercase_letters):
        index_lower = 0
        index_upper += 1
        
    i+=1
