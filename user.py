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

        last_name = last_name.strip()  # Remove leading/trailing spaces

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

def main():
    """
    Main function to get user input for first name and last name validation.
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

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
