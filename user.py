import re


def firstname(first_name):
    """
    Validates the given first name based on the following conditions:
    - The name must start with an uppercase letter.
    - The name can contain only alphabetic characters (both uppercase and lowercase).

    Parameters:
    first_name (str): The first name entered by the user.

    Returns:
    None: Prints whether the name is valid or invalid.
    """

    try:
        if not isinstance(first_name, str):
            raise TypeError("Input must be a string.")

        if re.match(r'^[A-Z][a-zA-Z]*$', first_name):
            print("Valid name")
        else:
            print("Invalid name. The first letter must be uppercase, and the name should contain only alphabets.")
    
    except TypeError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Get user input with exception handling
try:
    first_name = input("Enter your First name: ").strip()  # Stripping to remove unwanted spaces
    if not first_name:  # Check for empty input
        raise ValueError("Name cannot be empty.")
    firstname(first_name)
except ValueError as e:
    print(f"Error: {e}")


def lastname(last_name):
    """
    Validates the given last name based on the following conditions:
    - The name must start with an uppercase letter.
    - The name must contain only alphabetic characters.
    - The name must have at least 3 characters.

    Parameters:
    last_name (str): The last name entered by the user.

    Returns:
    None: Prints whether the name is valid or invalid.
    """

    try:
        if not isinstance(last_name, str):
            raise TypeError("Input must be a string.")

        last_name = last_name.strip()  # Remove leading/trailing spaces

        if len(last_name) < 3:
            raise ValueError("Invalid name. The name must have at least 3 characters.")

        if re.match(r'^[A-Z][a-zA-Z]*$', last_name):
            print("Valid name")
        else:
            raise ValueError("Invalid name. The first letter must be uppercase, and the name should contain only alphabets.")
    
    except ValueError as e:
        print(f"Error: {e}")

    except TypeError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Get user input with exception handling
try:
    last_name = input("Enter your last name: ").strip()
    if not last_name:  # Check for empty input
        raise ValueError("Name cannot be empty.")
    lastname(last_name)
except ValueError as e:
    print(f"Error: {e}")

def check_email(email):
    """
    Validates an email address based on the standard email format.

    Parameters:
    email (str): The email address entered by the user.

    Returns:
    bool: True if the email is valid, False otherwise.
    """

    try:
        if not isinstance(email, str):
            raise TypeError("Input must be a string.")

        email = email.strip()  # Remove leading/trailing spaces

        if not email:  # Check for empty input
            raise ValueError("Email cannot be empty.")

        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(regex, email):
            print(f"{email} is a Valid Email Address.")
            return True
        else:
            raise ValueError(f"{email} is an Invalid Email Address.")

    except ValueError as e:
        print(f"Error: {e}")
        return False

    except TypeError as e:
        print(f"Error: {e}")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

# Get user input with exception handling
try:
    email = input("Enter an email address: ").strip()
    check_email(email)
except Exception as e:
    print(f"Error: {e}")
    
