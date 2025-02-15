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
            print("Valid first name")
        else:
            print("Invalid first name. The first letter must be uppercase, and the name should contain only alphabets.")
    
    except TypeError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

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

        last_name = last_name.strip()

        if len(last_name) < 3:
            raise ValueError("Invalid last name. The name must have at least 3 characters.")

        if re.match(r'^[A-Z][a-zA-Z]*$', last_name):
            print("Valid last name")
        else:
            raise ValueError("Invalid last name. The first letter must be uppercase, and the name should contain only alphabets.")
    
    except ValueError as e:
        print(f"Error: {e}")

    except TypeError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

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

        email = email.strip()

        if not email:
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

def valid_mobileno(number):
    """
    Validates an Indian mobile number based on the following conditions:
    - It must start with '91' (India's country code), followed by a space.
    - It must be exactly 10 digits after the space.

    Parameters:
    number (str): The mobile number entered by the user.

    Returns:
    bool: True if the mobile number is valid, False otherwise.
    """
    try:
        if not isinstance(number, str):
            raise TypeError("Input must be a string.")

        pattern = r"^91\s\d{10}$"
        return bool(re.match(pattern, number))

    except TypeError as e:
        print(f"Error: {e}")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def valid_password(password):
    """
    Validates a password based on the following predefined rules:
    - Minimum 8 characters.
    - At least one uppercase letter.
    - At least one lowercase letter.
    - At least one digit.
    - At least one special character (!@#$%^&*).

    Parameters:
    password (str): The password entered by the user.

    Returns:
    bool: True if the password is valid, False otherwise.
    """
    try:
        if not isinstance(password, str):
            raise TypeError("Input must be a string.")

        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!])[A-Za-z\d@#$%^&*!]{8,}$'
        if re.match(pattern, password):
            print("Valid password")
            return True
        else:
            raise ValueError("Invalid password. Password must be at least 8 characters long and include an uppercase letter, a lowercase letter, a digit, and a special character.")

    except ValueError as e:
        print(f"Error: {e}")
        return False

    except TypeError as e:
        print(f"Error: {e}")
        return False

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False

def main():
    """
    Main function to get user input for first name, last name, email, mobile number, and password validation.
    """
    try:
        first_name = input("Enter your First name: ").strip()
        if not first_name:
            raise ValueError("First name cannot be empty.")
        firstname(first_name)

        last_name = input("Enter your Last name: ").strip()
        if not last_name:
            raise ValueError("Last name cannot be empty.")
        lastname(last_name)

        email = input("Enter an email address: ").strip()
        check_email(email)

        mob_numb = input("Enter your mobile number (Format: 91 XXXXXXXXXX): ").strip()
        if not mob_numb:
            raise ValueError("Mobile number cannot be empty.")

        while not valid_mobileno(mob_numb):
            print("Invalid mobile number. Please enter again.")
            mob_numb = input("Enter your mobile number (Format: 91 XXXXXXXXXX): ").strip()
            if not mob_numb:
                raise ValueError("Mobile number cannot be empty.")

        print("Your mobile number is valid:", mob_numb)

        password = input("Enter your password: ").strip()
        while not valid_password(password):
            print("Invalid password. Please try again.")
            password = input("Enter your password: ").strip()

        print("Password successfully set!")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
