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

def main():
    """
    Main function to get user input and validate the first name.
    """
    try:
        first_name = input("Enter your First name: ").strip()  # Stripping to remove unwanted spaces
        if not first_name:  # Check for empty input
            raise ValueError("Name cannot be empty.")
        firstname(first_name)
    except ValueError as e:
        print(f"Error: {e}")

# Ensuring the script runs only when executed directly
if __name__ == "__main__":
    main()
