def validate_name(name):
    """
    Validates if a name is valid.
    
    Args:
        name (str): The name to validate
        
    Returns:
        tuple: (is_valid, error_message) where is_valid is bool and error_message is str or None
    """
    if not isinstance(name, str):
        return False, "Input must be a string."
    
    if len(name) == 0:
        return False, "Please enter a valid name."
    
    if len(name) > 15:
        return False, "Name must be no more than 15 characters. Try again."
    
    if not name.isalpha():
        return False, "Name must contain only letters. No numbers or special characters allowed."
    
    return True, None


if __name__ == "__main__":
    while True:
        name = input("What is your name? ")
        is_valid, error_message = validate_name(name)
        if is_valid:
            break
        else:
            print(error_message)

    print(f"Hello {name}!")
    print("Welcome to the Copilot Lab!")
    print("This is a simple Python program that greets the user by name.")