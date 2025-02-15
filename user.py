import re


def firstname(first_name):
    name_len=len(first_name)
    if re.match(r'^[A-Z][a-zA-Z]*$', first_name):
        print("valid name")
    else:
        print("Invalid name")

first_name = str(input("Enter your First name "))
firstname(first_name)